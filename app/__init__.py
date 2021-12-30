"""
This is the __init__.py file for hospital_app module.
Imports all the necessary modules and submodules.
Defines all the needed variables for proper app functioning
"""
# standard library imports
import os

from app.logging import create_logger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration import Config
from flask_login import LoginManager
from flask_migrate import Migrate

database = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    # create logger
    create_logger()
    # create app
    app = Flask(__name__)
    app.config.from_object(Config)
    # to create an api and register the routes

    from .rest import create_api
    create_api(app)

    database.init_app(app)
    login_manager.init_app(app)
    # migrate database
    Migrate(app, database, directory=os.path.join('hospital_app', 'migrations'))
    from .views import user as user_blueprint
    login_manager.init_app(app)
    from .models.admin import Admin

    app.register_blueprint(user_blueprint)
    return app
