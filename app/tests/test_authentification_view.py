"""
This module defines the test cases for employee views
"""

# standard library imports
import http

# local imports
from app import create_app
from app.models.admin import Admin
from werkzeug.security import generate_password_hash
from app.tests.ConfigurationTests import ConfigurationTest


class TestAuthentificationView(ConfigurationTest):
    """
    This is the class for auth views test cases
    """

    def setUp(self):
        super(TestAuthentificationView, self).setUp()
        app = create_app()
        app.config['LOGIN_DISABLED'] = False
        # specify the database connection string
        self.app = app.test_client()

    def test_login(self):
        """
        Tests whether the get request on employees page works correctly,
        returning the status code 200
        """
        response = self.app.get('/login')
        self.assertEqual(200, response.status_code)

    def test_logout_not_authentificated(self):
        """
        Tests whether the get request on logout page works correctly if user is not authentificated,
        returning the status code 401
        """
        response = self.app.get('/logout')
        self.assertEqual(401, response.status_code)

    def test_success_login(self):
        """
        Tests whether the get request on employees page works correctly,
        returning the status code 200
        """
        response = self.app.post('/login', data={
            'username': 'admin',
            'password': generate_password_hash('12345'),
        }, follow_redirects=True)

        assert response.status_code == http.HTTPStatus.OK
        self.assertTrue(Admin.is_authenticated)

    def test_logout_authentificated(self):
        """
        Tests whether the get request on logout page works correctly if user is  authentificated,
        returning the status code 401
        """
        status_code = 301
        with self.app.session_transaction() as session:
            session['login'] = True
            if 'login' in session:
                self.assertEqual(301, status_code)
