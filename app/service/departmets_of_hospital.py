"""
This module defines crud operations to work with departments table
"""
# local imports
from app import database
from ..models.hospital import Hospital


def get_hospital_department() -> list:
    """
    This function is used to select all records from hospital table
    :return: the list of all departments of hospital
    """
    departments = Hospital.query.all()
    return [department.json() for department in departments]


def add_department(name: str, to_do: str) -> None:
    """
    This function is used to add a new department to hospital  table
    :param name: the name of the department of hospital
    :param to_do: the description of the department
    """
    department = Hospital(name=name, to_do=to_do)
    database.session.add(department)
    database.session.commit()


def update_department(identifier: int, name: str, to_do: str) -> None:
    """
    This function is used to update an existing department
    :param identifier: the id of the department of hospital to update
    :param name: the name of the department of hospital to update
    :param to_do: the description of the department of hospital to update
    """
    department = Hospital.query.get_or_404(identifier)
    department.name = name
    department.to_do = to_do
    database.session.add(department)
    database.session.commit()


def delete_department(identifier: int) -> None:
    """
    This function is used to delete an existing department
    :param identifier: the id of the department of hospital to delete
    """
    department = Hospital.query.get_or_404(identifier)
    database.session.delete(department)
    database.session.commit()


def get_department_by_id(identifier: int):
    """
    This function is used to get the single department by id
    :param identifier: the id of the department of the hospital to get
    :return: the department with the specified id
    """
    department = Hospital.query.get(identifier)
    return department.json() if department is not None else None
