import graphene
from .book import AllBooks, BookByTitle
from .user import AllUsers, UserByUsername

class Query(graphene.ObjectType):
    all_books = AllBooks.Field()
    book_by_title = BookByTitle.Field()

    all_users = AllUsers.Field()
    user_by_username = UserByUsername.Field()
