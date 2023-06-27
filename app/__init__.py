from config import Config

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    # to whitelist cross origin requests for resources. for eg. to run Apollo graphQL sandbox
    CORS(app)
    app.config.from_object((set_environment_config()))

    db.init_app(app)

    # initialise models
    from app.models.User import User
    from app.models.Client import Client

    @app.before_first_request
    def initialize_database():
        # create db tables for initialised models
        db.create_all()

    @app.route('/')
    def hello_world():
        app.logger.debug("home route")
        return "Hello World"

    from app.schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app


def set_environment_config():
    if Config.ENV == "PRODUCTION":
        return 'config.ProductionConfig'
    elif Config.ENV == "DEVELOPMENT":
        return 'config.DevelopmentConfig'
