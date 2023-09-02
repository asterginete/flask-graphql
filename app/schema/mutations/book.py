import graphene
from app.models import Book as BookModel
from app import db
from app.schema.inputs import BookInput
from app.schema.types import BookType

class CreateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, input):
        book = BookModel(title=input.title, author=input.author)
        db.session.add(book)
        db.session.commit()
        return CreateBook(book=book)

class UpdateBook(graphene.Mutation):
    class Arguments:
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(root, info, input):
        book = db.session.query(BookModel).filter_by(id=input.id).first()
        if book:
            book.title = input.title
            book.author = input.author
            db.session.commit()
        return UpdateBook(book=book)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        book = db.session.query(BookModel).filter_by(id=id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return DeleteBook(success=True)
        return DeleteBook(success=False)
