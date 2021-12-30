"""
This module defines the test cases for department views
"""

# local imports
from app import database
from app.models.hospital import Hospital
from app.tests.ConfigurationTests import ConfigurationTest


class TestDepartmentOfHospitalViews(ConfigurationTest):
    """
    This is the class for department of hospital views test cases
    """

    def test_homepage(self):
        """
        Tests whether the get request on homepage page works correctly,
        returning the status code 200
        """
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_departments_of_hospital(self):
        """
        Tests whether the get request on departments page works correctly,
        returning the status code 200
        """
        response = self.app.get('/departments')
        self.assertEqual(200, response.status_code)

    def test_add_departments_of_hospital(self):
        """
        Tests whether the get request on add department page works correctly,
        returning the status code 200
        """
        response = self.app.get('/departments/add')
        self.assertEqual(200, response.status_code)

    def test_edit_department(self):
        """
        Tests whether the get request on edit department page works correctly,
        returning the status code 200
        """
        department = Hospital(name="first hospital", to_do="something do")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/departments/edit/1')
        self.assertEqual(200, response.status_code)

    def test_delete_department(self):
        """
        Tests whether the get request on delete department page works correctly,
        returning the status code 200
        """
        department = Hospital(name="first hospital8", to_do="2")
        database.session.add(department)
        database.session.commit()
        response = self.app.get('/departments/delete/1')
        self.assertEqual(302, response.status_code)
