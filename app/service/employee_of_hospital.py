"""
This module defines crud operations to work with departments table
"""
# standard library imports
import re
import time
from datetime import datetime

# local imports
from app import database
from ..models.employee import Employee


def get_employees() -> list:
    """
    This functiion selects aall records from employee database
    :return: list
    """
    employees = Employee.query.all()
    return [employee.json() for employee in employees]


def get_employee_by_id(id_number: int):
    """
    This function is used to get the single employee by id
    :param id_number: the id of the employee to get
    :return: the employee with the specified id
    """
    employee = Employee.query.get(id_number)

    return employee.json() if employee is not None else None


def born_between_dates(start_date: str, end_date: str) -> list:
    """
    This function is used to get all the employees born between specified end and start dates
    :param start_date: the date to start comparison with
    :param end_date: the date to end comparison with
    :return: the list of employees born between specified end and start dates
    """
    start_date = time.strptime(start_date, '%m/%d/%Y')
    end_date = time.strptime(end_date, '%m/%d/%Y')
    employees = Employee.query.filter(Employee.date_of_birth.between(start_date, end_date))
    return [employee.json() for employee in employees]


def born_on_date(date: str) -> list:
    """
    This function is used to get all the employees born on a specified date
    :param date: the date to filter with
    :return: the list of employees born on a specified date
    """
    regex_date = re.sub("[^0-9/]", "", date)
    date = time.strptime(regex_date, '%m/%d/%Y')
    employees = Employee.query.filter_by(date_of_birth=date)
    return [employee.json() for employee in employees]


def add_employee(name: str, date_of_birth: str, salary: int, hospital_id: int) -> None:
    """
    This function is used to add a new employee to employees table
    :param name: the name of the employee
    :param date_of_birth: the date of birth of the employee, in format '%m/%d/%Y'
    :param salary: the salary of the employee
    :param hospital_id: id of department of hospital where employee works
    "
    """
    date_of_birth = time.strptime(date_of_birth, '%m/%d/%Y')
    employee = Employee(name=name, date_of_birth=date_of_birth, hospital_id=hospital_id, salary=salary)
    database.session.add(employee)
    database.session.commit()


def update_employee(identifier: int, name: str, salary: int, date_of_birth: str,  hospital_id: int) -> None:
    """
    This function is used to add a new employee to employees table
    :param identifier: id employee to change
    :param name: the name of the employee
    :param date_of_birth: the date of birth of the employee, in format '%m/%d/%Y'
    :param salary: the salary of the employee
    :param hospital_id: id of department of hospital where employee works
    "
    """
    employee = Employee.query.get_or_404(identifier)
    employee.name = name
    employee.hospital_id = hospital_id if hospital_id != '' else None
    employee.salary = salary
    employee.date_of_birth = datetime.strptime(date_of_birth, '%m/%d/%Y')
    database.session.add(employee)
    database.session.commit()


def delete_employee(identifier: int) -> None:
    """
    This function is used to delete an existing employee
    :param identifier: the id of the employee to delete
    """
    employee = Employee.query.get_or_404(identifier)
    database.session.delete(employee)
    database.session.commit()
