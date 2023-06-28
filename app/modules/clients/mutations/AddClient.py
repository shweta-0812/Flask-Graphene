from graphene import Mutation, String, Boolean
from app.models.Client import Client as ClientModel
from graphql import GraphQLError


class AddClient(Mutation):
    status = String(description="Request status")
    message = String(description="Request message")

    class Input:
        name = String(description="name of the client")

    def mutate(self, info, **kwargs):
        client = ClientModel(**kwargs)
        try:
            client.save()
        except Exception as e:
            raise GraphQLError("Error creating client object", e)
        else:
            return AddClient(status="SUCCESS", message="Client successfully created")
