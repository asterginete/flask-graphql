import graphene
from .book import CreateBook, UpdateBook, DeleteBook
from .user import CreateUser, UpdateUser, DeleteUser
from .notification import CreateNotification, UpdateNotification, DeleteNotification

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

    create_notification = CreateNotification.Field()
    update_notification = UpdateNotification.Field()
    delete_notification = DeleteNotification.Field()
