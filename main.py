from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from graphene import ObjectType, String, Int, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
principals = Principal(app)
admin_permission = Permission(RoleNeed('admin'))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True)
    password = db.Column(db.String(256))
    role = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('graphql'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    author = db.Column(db.String(256))

class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node, )

class Query(ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookObject)
    book_by_title = Field(List(BookObject), title=String(required=True))

    def resolve_book_by_title(self, info, title):
        return Book.query.filter_by(title=title).all()

class CreateBook(graphene.Mutation):
    class Arguments:
        title = String(required=True)
        author = String(required=True)

    book = Field(lambda: BookObject)

    def mutate(self, info, title, author):
        book = Book(title=title, author=author)
        db.session.add(book)
        db.session.commit()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        id = Int(required=True)
        title = String()
        author = String()

    book = Field(lambda: BookObject)

    def mutate(self, info, id, title, author):
        book = db.session.query(Book).filter_by(id=id).first()
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            db.session.commit()
            return UpdateBook(book=book)
        return None

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = Int(required=True)

    success = Int()

    def mutate(self, info, id):
        book = db.session.query(Book).filter_by(id=id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return DeleteBook(success=1)
        return DeleteBook(success=0)

class Mutation(ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
