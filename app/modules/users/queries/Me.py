from graphene import ObjectType, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType
# from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.User import User as UserModel
from app.models.Client import Client as ClientModel
from graphql import GraphQLError
from flask import current_app as flask_app
from app.modules.clients.queries import ClientType


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("password", )


class Me(ObjectType):
    # this defines a Field `me` in our Schema with a no Argument and response type user object
    me = Field(
        UserType,
        description=
    """
    :required: Access Token.
    :description: Returns the user object
    """
    )
    get_client = Field(ClientType)

    # Resolver method for me Field type takes the GraphQL context (self, info) as well as
    # Argument if any for the Field and returns data for the query Response

    # disable jwt
    # @jwt_required
    def resolve_me(self, info):
        # id = get_jwt_identity()
        id = 1
        user = UserModel.query.filter_by(id=id).scalar()
        if user:
            return user
        else:
            raise GraphQLError("User is not found.")

    def resolve_get_client(self, info):
        flask_app.logger.info(f"::::::info::::::::::{info}")
        client = ClientModel.query.filter_by(client_id=1).first()
        if client:
            return client
        else:
            raise GraphQLError("User client details not found")

