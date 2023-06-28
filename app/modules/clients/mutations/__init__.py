from graphene import AbstractType

from .AddClient import AddClient
# from .UpdateClient import UpdateClient
# from .DeleteClient import DeleteClient


class ClientMutation(AbstractType):
    add_client = AddClient.Field()
    # update_client = UpdateClient.Field()
    # delete_client = DeleteClient.Field()