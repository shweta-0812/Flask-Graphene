from graphene import ObjectType, Field
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
from app.models.Client import Client as ClientModel


class ClientType(SQLAlchemyObjectType):
    class Meta:
        model = ClientModel


class GetClient(ObjectType):
    client = Field(ClientType, description=" Returns Client Object")

    def resolve_client(self, info):
        print(info)
        id = 1
        client = ClientModel.query.filter_by(id=id).scalar()

        if client:
            return client
        else:
            raise GraphQLError("Client not found")