from graphene import Mutation, Boolean, String
from app.models.User import User as UserModel
from graphql import GraphQLError


class RegisterUser(Mutation):
    # response attributes
    status = Boolean(description="Request status")
    message = String(description="Request message")

    class Input:
        email = String(description="Self Descriptive")
        password = String(description="Self Descriptive")

    def mutate(self, info, **kwargs):
        user = UserModel(**kwargs)
        try:
            user.save()
        except Exception as e:
            raise GraphQLError("Error creating User object.", e)
        else:
            return RegisterUser(status=True, message="User have been created successfully")
