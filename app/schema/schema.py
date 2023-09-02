from graphene import Schema
from app.schema.queries import Query
from app.schema.mutations import Mutation

schema = Schema(query=Query, mutation=Mutation)
