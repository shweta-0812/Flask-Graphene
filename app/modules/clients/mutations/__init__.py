from graphene import AbstractType

from .RegisterClient import RegisterClient


class ClientMutation(AbstractType):
    register_client = RegisterClient.Field()