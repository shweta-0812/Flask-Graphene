from graphene import ObjectType, Field
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from app.models.Client import Client as ClientModel
from app.models.User import User as UserModel


# custom data type for response to query
class ClientType(SQLAlchemyObjectType):
    class Meta:
        model = ClientModel


class GetClient(ObjectType):
    client = Field(ClientType, description=" Returns Client Object")

    # all_client_users =
    def resolve_client(self, info):
        id = 1  # pass id as an argument or username as an argument
        client = ClientModel.query.filter_by(id=id).scalar()

        if client:
            return client
        else:
            raise GraphQLError("Client not found")
