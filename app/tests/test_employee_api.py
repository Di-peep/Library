"""
This module defines the test cases for employee api
"""
# standard library imports
import json

# local imports
from datetime import datetime

from app import database
from app.models.employee import Employee
from app.tests.ConfigurationTests import ConfigurationTest


class TestEmployeeApi(ConfigurationTest):
    """
    This is the class for employee api test cases
    """

    def test_abort_if_employee_doesnt_exist(self):
        """
        Test whether the page aborts with status code 404 if there are no record with
        the specified id in the database
        """
        response = self.app.delete('/api/employees/10')
        self.assertEqual(404, response.status_code)

    def test_get_employees(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        date_2 = datetime.strptime('12/07/2021', '%m/%d/%Y').date()
        employee_1 = Employee(name='Api Name 1', salary=2500, date_of_birth=date_1)
        employee_2 = Employee(name='Api Name 2', salary=2600, date_of_birth=date_2)
        database.session.add(employee_1)
        database.session.add(employee_2)
        database.session.commit()
        response = self.app.get('/api/employees')
        self.assertEqual(200, response.status_code)

    def test_get_single_employee(self):
        """
        Adds 1 test record and tests whether the get request to /api/employees/<id>
        works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        employee_1 = Employee(name='Api test', salary=1500, date_of_birth=date_1)
        database.session.add(employee_1)
        database.session.commit()
        response = self.app.get('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_post_employee(self):
        """
        Forms a json object and tests whether the post request to /api/employees
        works correctly, returning the status code 201
        """
        employee = {
            'name': 'test api',
            'salary': 1500,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.post('/api/employees', data=json.dumps(employee), content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_put_employee(self):
        """
        Adds 1 test record, forms a json object and tests whether the put request to
        /api/employees/<id> works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        employee = Employee(name="test1", salary=2300, date_of_birth=date_1)
        database.session.add(employee)
        database.session.commit()
        employee = {
            'name': 'updated',
            'salary': 1000,
            'date_of_birth': '02/23/1961'}
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete_employee(self):
        """
        Adds 1 test record and tests whether the delete request to /api/employees/<id>
        works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        employee = Employee(name="test1", salary=2300, date_of_birth=date_1)
        database.session.add(employee)
        database.session.commit()
        response = self.app.delete('/api/employees/1')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_on(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        with date parameter (search for employees born on specific date) works
        correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        employee = Employee(name="test1", salary=2300, date_of_birth=date_1)
        date_2 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_2 = Employee(name="test1", salary=2300, date_of_birth=date_2)
        database.session.add(employee)
        database.session.add(employee_2)
        database.session.commit()
        response = self.app.get('/api/employees?date=02/23/2021')
        self.assertEqual(200, response.status_code)

    def test_get_employees_born_between(self):
        """
        Adds 3 test records and tests whether the get request to /api/employees
        with start_date and end_date parameters (search for employees born on specific date range)
        works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        employee_1 = Employee(name="test1", salary=2300, date_of_birth=date_1)
        date_2 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_2 = Employee(name="test1", salary=2300, date_of_birth=date_2)
        date_3 = datetime.strptime('02/23/1990', '%m/%d/%Y').date()
        employee_3 = Employee(name="test1", salary=2300, date_of_birth=date_3)
        database.session.add(employee_1)
        database.session.add(employee_2)
        database.session.add(employee_3)
        database.session.commit()
        response = self.app.get('/api/employees?start_date=05/15/1990&end_date=05/20/2022')
        self.assertEqual(200, response.status_code)

    def test_search_on_invalid_date(self):
        """
        Adds 2 test records and tests whether the get request to /api/employees
        with invalid date parameter (search for employees born on specific date) works
        correctly, returning the status code 400
        """
        date_1 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_1 = Employee(name="test1", salary=2300, date_of_birth=date_1)
        date_2 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_2 = Employee(name="test1", salary=2300, date_of_birth=date_2)
        database.session.add(employee_1)
        database.session.add(employee_2)
        database.session.commit()
        response = self.app.get('/api/employees?date=05/23/2021sdfdsafz')
        self.assertEqual(400, response.status_code)

    def test_adding_none_values(self):
        """
        Forms a json object with none values and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': None,
            'salary': None,
            'date_of_birth': None
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_adding_empty_values(self):
        """
        Forms a json object with empty values and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': '',
            'salary': '',
            'date_of_birth': ''
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_adding_negative_salary(self):
        """
        Forms a json object with negative salary value and tests whether the post request to
        /api/employees works correctly, returning the status code 400
        """
        employee = {
            'name': 'name1',
            'salary': -1000,
            'date_of_birth': '02/23/1990'
        }
        response = self.app.post('/api/employees',
                                 data=json.dumps(employee),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_negative_salary(self):
        """
        Adds 1 test record, forms a json object with negative salary value values and tests
        whether the put request to /api/employees/<id> works correctly, returning the status code 400
        """
        date_1 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_1 = Employee(name="test1", salary=2300, date_of_birth=date_1)
        database.session.add(employee_1)
        database.session.commit()
        employee = {
            'name': 'changed',
            'salary': -11111,
            'date_of_birth': '02/23/2000'
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_empty_values(self):
        """
        Adds 1 test record, forms a json object with empty values and tests whether the
        put request to /api/employees/<id> works correctly, returning the status code 400
        """
        date_1 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_1 = Employee(name="test1", salary=2300, date_of_birth=date_1)
        database.session.add(employee_1)
        database.session.commit()
        employee = {
            'name': '',
            'salary': '',
            'date_of_birth': ''
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_none_values(self):
        """
        Adds 1 test record, forms a json object with none values and tests whether the
        put request to /api/employees/<id> works correctly, returning the status code 200
        """
        date_1 = datetime.strptime('02/23/2001', '%m/%d/%Y').date()
        employee_1 = Employee(name="test1", salary=2300, date_of_birth=date_1)
        database.session.add(employee_1)
        database.session.commit()
        employee = {
            'name': None,
            'salary': None,
            'date_of_birth': None
        }
        response = self.app.put('/api/employees/1',
                                data=json.dumps(employee),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)
