from graphene import ObjectType, Schema, String

from app.modules.users.queries import UserQuery
from app.modules.users.mutations import UserMutation
from app.modules.clients.mutations import ClientMutation
from app.modules.clients.queries import ClientQuery


class RootQuery(UserQuery, ClientQuery, ObjectType):
    pass


class RootMutation(UserMutation, ClientMutation, ObjectType):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
