from graphene import ObjectType

from .GetClient import GetClient


class ClientQuery(GetClient, ObjectType):
    pass
