"""Specify configurations"""
from datetime import timedelta


class Config(object):
    """
    Base configuration
    """
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)
    MAX_CONTENT_LENGTH = 1024 * 1024
    SECRET_KEY = '7b0342f12ee64296aaaa9738c72ca2c4'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/hospital_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(object):
    """
    Testing configurations
    """

    # Activates the testing mode of Flask extensions. This allows us to use testing properties
    # that could for instance have an increased runtime cost, such as unittest helpers.
    TESTING = True
    SQLALCHEMY_ECHO = False
