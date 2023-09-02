import graphene

class UserInput(graphene.InputObjectType):
    id = graphene.Int()
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String()
