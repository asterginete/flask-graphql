import graphene
from app.models import User as UserModel
from app import db
from app.schema.inputs import UserInput
from app.schema.types import UserType

class CreateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, input):
        user = UserModel(username=input.username, email=input.email)
        user.password = input.password
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        input = UserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(root, info, input):
        user = db.session.query(UserModel).filter_by(id=input.id).first()
        if user:
            user.username = input.username
            user.email = input.email
            if input.password:
                user.password = input.password
            db.session.commit()
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(root, info, id):
        user = db.session.query(UserModel).filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return DeleteUser(success=True)
        return DeleteUser(success=False)
