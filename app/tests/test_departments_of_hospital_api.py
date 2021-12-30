"""
This module defines the test cases for department api
"""
# standard library imports
import json

# local imports
# pylint: disable=import-error
from hospital_app import database
from hospital_app.models.hospital import Hospital
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestDepartmentApi(ConfigurationTest):
    """
    This is the class for department of hospital api test cases
    """

    def test_get_departments_of_hospital(self):
        """
        Adds 2 test records and tests whether the get request to /api/hospitals
        works correctly, returning the status code 200
        """
        department1 = Hospital(name="ApiTest1", to_do="something1")
        department2 = Hospital(name="ApiTest2", to_do="something2")
        database.session.add(department1)
        database.session.add(department2)
        database.session.commit()
        response = self.app.get('/api/departments')
        self.assertEqual(200, response.status_code)

    def test_get_single_department_of_hospital(self):
        """
        Adds 1 test record and tests whether the get request to /api/hospitals/<id>
        works correctly, returning the status code 200
        """
        department1 = Hospital(name='ApiTest1', to_do="something2")
        database.session.add(department1)
        database.session.commit()
        response = self.app.get('/api/departments/1')
        self.assertEqual(200, response.status_code)

    def test_abort_if_department_of_hospital_doesnt_exist(self):
        """
        Test whether the page aborts with status code 404 if there are no record with
        the specified id in the database
        """
        response = self.app.delete('/api/departments/10')
        self.assertEqual(404, response.status_code)

    def test_post_department_of_hospital(self):
        """
        Forms a json object and tests whether the post request to /api/hospitals
        works correctly, returning the status code 201
        """
        hospital = {
            'name': 'ApiTest1',
            'to_do': 'something doing'
        }
        response = self.app.post('/api/departments',
                                 data=json.dumps(hospital),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)

    def test_put_department_of_hospital(self):
        """
        Adds 1 test record, forms a json object and tests whether the put request to
        /api/hospitals/<id> works correctly, returning the status code 200
        """
        hospital = Hospital(name="ApiTest1", to_do="something doing")
        database.session.add(hospital)
        database.session.commit()
        hospital = {
            'name': 'ApiTest2',
            'to_do': 'something doing2'
        }
        response = self.app.put('/api/departments/1',
                                data=json.dumps(hospital),
                                content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete_department_of_hospital(self):
        """
        Adds 1 test record and tests whether the delete request to /api/hospitals/<id>
        works correctly, returning the status code 200
        """
        hospital = Hospital(name="Api testing", to_do="to do")
        database.session.add(hospital)
        database.session.commit()
        response = self.app.delete('/api/departments/1')
        self.assertEqual(200, response.status_code)

    def test_adding_none_values(self):
        """
        Forms a json object with none values and tests whether the post request to
        /api/hospitals works correctly, returning the status code 400
        """
        hospital = {
            'name': None,
            'to_do': None
        }
        response = self.app.post('/api/departments',
                                 data=json.dumps(hospital),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_empty_data_sended(self):
        """
        Forms a json object with empty values and tests whether the post request to
        /api/hospitals works correctly, returning the status code 400
        """
        hospital = {
            'name': '',
            'to_do': ''
        }
        response = self.app.post('/api/departments',
                                 data=json.dumps(hospital),
                                 content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_none_name(self):
        """
        Adds 1 test record, forms a json object with none name value and tests whether the
        put request to /api/hospitals/<id> works correctly, returning the status code 200
        """
        hospital = Hospital(name="Api testing", to_do="to do")
        database.session.add(hospital)
        database.session.commit()
        hospital2 = {
            'name': None,
            'to_do': 'updated'
        }
        response = self.app.put('/api/departments/1',
                                data=json.dumps(hospital2),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_none_description(self):
        """
        Adds 1 test record, forms a json object with none description value and tests whether the
        put request to /api/hospitals/<id> works correctly, returning the status code 200
        """
        hospital = Hospital(name="Api testing", to_do="to do")
        database.session.add(hospital)
        database.session.commit()
        hospital2 = {
            'name': None,
            'to_do': 'updated'
        }
        response = self.app.put('/api/departments/1',
                                data=json.dumps(hospital2),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)

    def test_editing_empty_description(self):
        """
        Adds 1 test record, forms a json object with empty description value and tests whether the
        put request to /api/hospitals/<id> works correctly, returning the status code 400
        """
        hospital = Hospital(name="Api testing", to_do="to do")
        database.session.add(hospital)
        database.session.commit()
        host = {
            'name': 'updated',
            'to_do': ''
        }
        response = self.app.put('/api/departments/1',
                                data=json.dumps(host),
                                content_type='application/json')
        self.assertEqual(400, response.status_code)
