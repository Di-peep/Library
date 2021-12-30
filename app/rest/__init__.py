"""This is the __init__.py file of rest module.
Imports the department_of_hospital_api and employee_api submodules and registers the api links
"""
# standard library imports
from flask_restful import Api


# local imports
from . import department_of_hospital_api
from . import employees_api


def create_api(application):
    api = Api(application)

    # adding the department resources
    api.add_resource(department_of_hospital_api.AllDepartments, '/api/departments')
    api.add_resource(department_of_hospital_api.SingleDepartment, '/api/departments/<identifier>')

    # adding the employee resources
    api.add_resource(employees_api.AllEmployees, '/api/employees')
    api.add_resource(employees_api.SingleEmployee, '/api/employees/<identifier>')

    return api
