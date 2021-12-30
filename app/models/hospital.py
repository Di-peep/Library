"""
Department model used to represent departments, this module defines the
following classes:
- `Hospital`, hospital model
"""

from app import database


class Hospital(database.Model):
    """
    Create a department table
    Fields:
        id: the unique identifier of the department, primary key
        name: the name of the department, unique
        to_do: what department do
    """

    #: Name of the database table storing departments of hospital
    __tablename__ = 'hospital'

    #: Database id of the department of hospital
    id = database.Column(database.Integer, primary_key=True)

    #: Name of the department
    name = database.Column(database.String(64), unique=True)

    #: what department doing
    to_do = database.Column(database.String(255), unique=True)

    #: employees of department
    employees = database.relationship('Employee', backref='hospital',
                                      lazy='dynamic')

    def json(self):
        """
        This method is used to return the department in json format
        :return: the department in json format
        """
        return {
            'id': self.id,
            'name': self.name,
            'to_do': self.to_do,
            'employees': [employee.json() for employee in self.employees]
        }

    def __repr__(self):
        """
        The representation of the department
        :return: the string, representing the department of hospital by its name
        """
        return '<Hospital: {}>'.format(self.name)
