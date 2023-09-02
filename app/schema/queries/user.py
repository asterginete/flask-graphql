import graphene
from app.models import User as UserModel
from app.schema.types import UserType

class AllUsers(graphene.Field):
    class Meta:
        type_ = graphene.List(UserType)

    def resolve(self, info):
        return UserModel.query.all()

class UserByUsername(graphene.Field):
    class Arguments:
        username = graphene.String(required=True)

    class Meta:
        type_ = UserType

    def resolve(self, info, username):
        return UserModel.query.filter_by(username=username).first()
