"""
This module defines a rest interface to work with employees
"""
import re
import time
from flask import abort, jsonify, request, Response
from flask_restful import reqparse, Resource

# local imports
from ..service import employee_of_hospital

# get the request parser
parser = reqparse.RequestParser()
# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('salary')
parser.add_argument('date_of_birth')
parser.add_argument('hospital_id')


def validate_date(date):
    """
    This function checks whether th date matches the mm/dd/yyyy pattern
    :param date: date to check
    :return: true, if date matches the pattern, false if not
    """

    if re.search('[a-zA-Zа-яА-ЯҐґ]', date):
        return False
    try:
        return bool(time.strptime(date, '%m/%d/%Y'))
    except ValueError:
        return False


def abort_if_employee_doesnt_exist(identifier):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param identifier: the id of the resource
    """
    if employee_of_hospital.get_employee_by_id(identifier) is None:
        abort(Response("Employee {} doesn't exist".format(identifier), 404))


class AllEmployees(Resource):
    """
     This is the class for EmployeeList Resource available at /employees url
     """

    @staticmethod
    def get():
        """
        This method is called when GET request is sent
        :return: the list of all employees in json format
        """
        args = request.args
        if len(args) == 2 and validate_date(args['start_date']) and validate_date(args['end_date']):
            return jsonify(employee_of_hospital.born_between_dates(start_date=args['start_date'],
                                                                   end_date=args['end_date']))
        if len(args) == 1 and validate_date(args['date']):
            return jsonify(employee_of_hospital.born_on_date(date=args['date']))
        if len(args) == 0:
            return jsonify(employee_of_hospital.get_employees())

        return abort(Response("Couldn't perform search. Invalid data", 400))

    @staticmethod
    def post():
        """
        This method is called when POST request is sent
        :return: the 'Employee added' response with status code 201
        """
        args = parser.parse_args()
        if args['name'] is None or args['salary'] is None or args['date_of_birth'] is None:
            abort(Response("Couldn't add employee. Missing data", 400))
        elif args['name'] == '' or args['salary'] == '' or args['date_of_birth'] == '':
            abort(Response("Couldn't add employee. Missing or invalid data", 400))
        elif int(args['salary']) < 0 or not validate_date(args['date_of_birth']):
            abort(Response("Couldn't add employee. Missing or invalid data", 400))
        else:
            employee_of_hospital.add_employee(args['name'],
                                              args['date_of_birth'],
                                              args['salary'], args['hospital_id'])
            return "Employee added", 201


class SingleEmployee(Resource):
    """
    This is the class for Employee Resource available at /employees/<id> url
    """

    @staticmethod
    def get(identifier):
        """
        This method is called when GET request is sent
        :return: the specific employee in json format
        """
        abort_if_employee_doesnt_exist(identifier)
        return jsonify(employee_of_hospital.get_employee_by_id(identifier))

    @staticmethod
    def put(identifier):
        """
        This method is called when PUT request is sent
        :return: the 'Employee updated' response with status code 200
        """
        args = parser.parse_args()
        single_employee = employee_of_hospital.get_employee_by_id(identifier)
        if args['name'] == '' or args['salary'] == '' or args['date_of_birth'] == '':
            abort(Response("Couldn't edit employee. Missing or invalid data", 400))
        if (args['salary'] is not None and int(args['salary']) < 0) or (
                args['date_of_birth'] is not None and not validate_date(args['date_of_birth'])):
            abort(Response("Couldn't edit employee. Missing or invalid data", 400))
        if args['name'] is None:
            args['name'] = single_employee['name']
        if args['date_of_birth'] is None:
            args['date_of_birth'] = single_employee['date_of_birth']
        if args['salary'] is None:
            args['salary'] = single_employee['salary']
        employee_of_hospital.update_employee(identifier,
                                             args.get('name', single_employee['name']),
                                             args.get('salary', single_employee['salary']),
                                             args.get('date_of_birth', single_employee['date_of_birth']),
                                             args.get('hospital_id', single_employee['hospital_id']))
        return "Employee updated", 200

    @staticmethod
    def delete(identifier):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_employee_doesnt_exist(identifier)
        employee_of_hospital.delete_employee(identifier)
        return 'Employee deleted', 200
