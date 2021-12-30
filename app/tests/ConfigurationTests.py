"""
This mpdule representate base configuration class of test
"""
# standard library imports
import unittest

# local imports
from app import create_app, database
from configuration import TestingConfig


class ConfigurationTest(unittest.TestCase):
    """
    Create a configuration test case
    """

    def setUp(self):
        # create the app with the specified config
        app = create_app()
        app.config['LOGIN_DISABLED'] = True
        app.config.from_object(TestingConfig)
        # specify the database connection string
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test_hospital_app'
        database.init_app(app)
        with app.app_context():
            database.create_all()
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        """
        This method is executed after every test case
        :return:
        """
        # close all the session and drop the tables
        database.session.close_all()
        database.drop_all()
