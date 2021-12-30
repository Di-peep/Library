"""
Employee model used to represent employees, this module defines the
following classes:
- `Employee`, employee model
"""

from app import database
from .hospital import Hospital


class Employee(database.Model):
    """
    Create an employee table
    Fields:
        id: the unique identifier of the employee, primary key
        name: the name of the employee
        date_of_birth: the date of birth of the employee
        salary: the salary of the employee
        hospital_id: the id of related department, foreign key to hospital.id

    """
    #: Name of the database table storing employees
    __tablename__ = 'employee'

    #: employee's database id
    id = database.Column(database.Integer, primary_key=True)

    #: employee's name
    name = database.Column(database.String(64), nullable=False)

    #: employee's date of birth
    date_of_birth = database.Column(database.Date, nullable=False)

    #: employee's salary
    salary = database.Column(database.Integer)

    #: database id of the department employee works in
    hospital_id = database.Column(database.Integer, database.ForeignKey('hospital.id'))

    def json(self):
        """
        This method is used to return the employee in json format
        :return: the employee in json format
        """
        # pylint: disable=no-member
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary, 'date_of_birth': self.date_of_birth.strftime('%m/%d/%Y'),
            'hospital_id': Hospital.query.get_or_404(self.hospital_id).name
            if self.hospital_id is not None else None
        }

    def __repr__(self):
        """
        The representation of the employee
        :return: the string, representing the employee by his name
        """
        return '<Employee: {}>'.format(self.name)
