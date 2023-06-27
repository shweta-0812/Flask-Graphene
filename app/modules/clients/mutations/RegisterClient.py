from graphene import Mutation, String, Boolean
from app.models.Client import Client as ClientModel
from graphql import GraphQLError


class RegisterClient(Mutation):
    status = Boolean(description="Request status")
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
            return RegisterClient(status=True, message="Client successfully created")
