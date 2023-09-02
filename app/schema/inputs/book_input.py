import graphene

class BookInput(graphene.InputObjectType):
    id = graphene.Int()
    title = graphene.String(required=True)
    author = graphene.String(required=True)
