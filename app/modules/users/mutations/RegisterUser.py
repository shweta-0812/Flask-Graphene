# from flask import current_app as flask_app

from graphene import Mutation, Boolean, String
from app.models.User import User as UserModel
from app.models.Client import Client as ClientModel
from graphql import GraphQLError


class RegisterUser(Mutation):
    # response attributes
    status = Boolean(description="Request status")
    message = String(description="Request message")

    class Input:
        # input arguments
        username = String(description="Self Descriptive")
        email = String(description="Self Descriptive")
        password = String(description="Self Descriptive")

    def mutate(self, info, **kwargs):
        def _get_client_name_from_email(email):
            email_parts = email.split('@')
            return email_parts[0]

        mutations_args = {**kwargs}
        client_name = _get_client_name_from_email(mutations_args["email"])
        client = ClientModel.query.filter_by(name=client_name).scalar()
        if not client:
            new_client = ClientModel(name=client_name)
            try:
                client = new_client.save()
            except Exception as e:
                raise GraphQLError("Error creating Client for User object.", e)

        # flask_app.logger.info(f"::::::client id::::::::::{client.id}")
        client_id = client.id
        user = UserModel(client_id=client_id, username=mutations_args["username"], email=mutations_args["email"],
                         password=mutations_args["password"])
        try:
            user.save()
        except Exception as e:
            raise GraphQLError("Error creating User object.", e)
        else:
            return RegisterUser(status=True, message="User have been created successfully")