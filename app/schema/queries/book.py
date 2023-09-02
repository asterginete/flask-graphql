import graphene
from app.models import Book as BookModel
from app.schema.types import BookType

class AllBooks(graphene.Field):
    class Meta:
        type_ = graphene.List(BookType)

    def resolve(self, info):
        return BookModel.query.all()

class BookByTitle(graphene.Field):
    class Arguments:
        title = graphene.String(required=True)

    class Meta:
        type_ = BookType

    def resolve(self, info, title):
        return BookModel.query.filter_by(title=title).first()
