"""
This module defines the test cases for profile views
"""
# standard library imports
import http

# local imports
from app import create_app
from app.models.admin import Admin
from werkzeug.security import generate_password_hash
from app.tests.ConfigurationTests import ConfigurationTest


class TestProfileView(ConfigurationTest):
    """
    This is the class for profile views test cases
    """

    def setUp(self):
        super(TestProfileView, self).setUp()

    def test_profile(self):
        """
        Tests whether the get request on profile page works correctly,
        returning the status code 200
        """
        app = create_app()
        app.config['LOGIN_DISABLED'] = False
        # specify the database connection string
        self.app = app.test_client()
        response = self.app.get('/profile')
        self.assertEqual(401, response.status_code)

    def test_not_auth_profile(self):
        """
        Tests whether the get request on profile page works correctly,
        returning the status code 401
        """
        app = create_app()
        app.config['LOGIN_DISABLED'] = False
        # specify the database connection string
        self.app = app.test_client()
        response = self.app.get('/profile')
        self.assertEqual(401, response.status_code)
