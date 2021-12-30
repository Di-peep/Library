"""
This module defines a rest interface to work with departments of hospital
"""
from flask import abort, jsonify, Response
from flask_restful import reqparse, Resource

# local imports
from ..service import departmets_of_hospital

# get the request parser
parser = reqparse.RequestParser()

# define the arguments which will be in a request query
parser.add_argument('name')
parser.add_argument('to_do')


def abort_if_department_doesnt_exist(identifier):
    """
    This function is used to prevent the access of a resource that doesn't exist
    :param identifier: the id of the resource
    """
    if departmets_of_hospital.get_department_by_id(identifier) is None:
        abort(Response("Department of hosptital {} doesn't exist".format(identifier), 404))


class AllDepartments(Resource):
    """
     This is the class for AllDepartments Resource available at /hospital url
    """

    @staticmethod
    def get():
        return jsonify(departmets_of_hospital.get_hospital_department())

    @staticmethod
    def post():
        """
        This method is called when POST request is sent
        :return: the 'Department added' response with status code 201
        """
        args = parser.parse_args()
        if args['name'] is None or args['to_do'] is None:
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        elif args['name'].strip() == '' or args['to_do'].strip() == '':
            abort(Response("Couldn't edit department. Missing data", 400))
        elif args['name'] == '' or args['to_do'] == '':
            abort(Response("Couldn't add department of hospital. Check insert data", 400))
        else:
            departmets_of_hospital.add_department(args['name'], args['to_do'])
        return "Department of hospital added", 201


class SingleDepartment(Resource):
    """
    This is the class for Department Resource available at /hospital/<id> url
    """

    @staticmethod
    def get(identifier):
        """
        This method is called when GET request is sent
        :return: the specific department in json format
        """
        abort_if_department_doesnt_exist(identifier)
        return jsonify(departmets_of_hospital.get_department_by_id(identifier))

    @staticmethod
    def delete(identifier):
        """
        This method is called when DELETE request is sent
        :return: the empty response with status code 204
        """
        abort_if_department_doesnt_exist(identifier)
        departmets_of_hospital.delete_department(identifier)
        return 'Department deleted', 200

    @staticmethod
    def put(identifier):
        """
        This method is called when PUT request is sent
        :return: the 'Department updated' response with status code 200
        """
        args = parser.parse_args()
        hospital = departmets_of_hospital.get_department_by_id(identifier)
        if args['name'] is None or args['to_do'] is None:
            abort(Response("Couldn't edit department. Missing data", 400))
        if args['name'] == '' or args['to_do'] == '':
            abort(Response("Couldn't edit department. Missing data", 400))
        if args['name'].strip() == '' or args['to_do'].strip() == '':
            abort(Response("Couldn't edit department. Missing data", 400))

        departmets_of_hospital.update_department(identifier, args.get('name', hospital['name']),
                                                 args.get('to_do', hospital['to_do']))
        return "Department updated", 200
