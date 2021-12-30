"""
This module defines the test cases for department service
"""

# local imports
from datetime import datetime
from hospital_app.models.employee import Employee
from hospital_app import database
from hospital_app.service import employee_of_hospital
from hospital_app.tests.ConfigurationTests import ConfigurationTest


class TestEmployeeService(ConfigurationTest):
    """
    This is the class for employee service test cases
    """

    def test_get_employees(self):
        """
        Adds 2 test records and tests whether the count of records is 2
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        date_2 = datetime.strptime('12/07/2021', '%m/%d/%Y').date()
        employee1 = Employee(name="name1", date_of_birth=date_1, salary=2000)
        employee2 = Employee(name="name2", date_of_birth=date_2, salary=2900)
        database.session.add(employee1)
        database.session.add(employee2)
        database.session.commit()
        self.assertEqual(2, len(employee_of_hospital.get_employees()))

    def test_add_employee(self):
        """
        Adds a new employee with specified parameters and tests whether the count
        of records is 1
        """
        employee_of_hospital.add_employee(name="Tests",
                                          salary=200, date_of_birth='07/07/2021', hospital_id=None)
        self.assertEqual(1, Employee.query.count())

    def test_delete_employee(self):
        """
        Adds a new employee with specified parameters, deletes it and tests
        whether the count of records is 0
        """
        date = datetime.strptime('09/09/2021', '%m/%d/%Y').date()
        employee = Employee(name="Test1", salary=2500, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        employee_of_hospital.delete_employee(1)
        self.assertEqual(0, Employee.query.count())

    def test_get_employee_by_id(self):
        """
        Adds 1 test record and tests whether the id of added record is 1
        """
        date = datetime.strptime('09/09/2021', '%m/%d/%Y').date()
        employee = Employee(name="Test1", salary=2500, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        self.assertEqual(1, employee_of_hospital.get_employee_by_id(1)['id'])

    def test_update_employee(self):
        """
        Adds a new employee with specified parameters, updates it with new parameters
        and tests whether the values updated
        """
        date = datetime.strptime('09/09/2021', '%m/%d/%Y').date()
        employee = Employee(name="Test1", salary=2500, date_of_birth=date)
        database.session.add(employee)
        database.session.commit()
        employee_of_hospital.update_employee(1, name="Changed", salary=200,
                                             date_of_birth='06/15/1990', hospital_id=None)
        employee = Employee.query.get(1)
        self.assertEqual("Changed", employee.name)

    def test_get_employees_born_on(self):
        """
        Adds 2 test records and tests whether the search for employees born on specific
        date works correctly and the count of records is 1
        """
        date_1 = datetime.strptime('02/23/2021', '%m/%d/%Y').date()
        date_2 = datetime.strptime('12/07/2021', '%m/%d/%Y').date()
        employee1 = Employee(name="Tests1", salary=2000, date_of_birth=date_1)
        employee2 = Employee(name="Tests2", salary=2900, date_of_birth=date_2)
        database.session.add(employee1)
        database.session.add(employee2)
        database.session.commit()
        self.assertEqual(1, len(employee_of_hospital.born_on_date("02/23/2021")))

    def test_get_employees_born_between(self):
        """
        Adds 2 test records and tests whether the search for employees born on specific
        date range works correctly and the count of records is 2
        """
        date_1 = datetime.strptime('02/23/2018', '%m/%d/%Y').date()
        date_2 = datetime.strptime('12/07/2022', '%m/%d/%Y').date()
        employee1 = Employee(name="Tests1", salary=2000, date_of_birth=date_1)
        employee2 = Employee(name="Tests2", salary=2900, date_of_birth=date_2)
        database.session.add(employee1)
        database.session.add(employee2)
        database.session.commit()
        self.assertEqual(2, len(employee_of_hospital.born_between_dates("12/12/2001",
                                                                        "12/12/2022")))
