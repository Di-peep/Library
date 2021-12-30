"""
This module defines is used to populate database with admin, hospital  and employees,
it defines the following:
Functions:
- `populate_database`: populate database with employees,admin and hospital
"""
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from app import create_app
from app.models.admin import Admin
from app.models.hospital import Hospital
from app.models.employee import Employee


def populate_database():
    """
    Populate database with employees,admin and hospital
    :return: None
    """
    database = SQLAlchemy(create_app())
    admin1 = Admin('admin', generate_password_hash('12345'), None, 'Vihor Dmytro')
    admin2 = Admin('dima', generate_password_hash('iwilly17'), None, 'Dima Dima')

    employee_1 = Employee(name='John Doe', salary=1300, date_of_birth=date(1999, 7, 12), hospital_id=97)
    employee_2 = Employee(name='Jane Wilson', salary=1300, date_of_birth=date(1993, 1, 8), hospital_id=98)
    employee_3 = Employee(name='Will Hunting', salary=1300, date_of_birth=date(1989, 11, 30), hospital_id=73)

    hospital_1 = Hospital(name='Paramedical', to_do='something do1')
    hospital_2 = Hospital(name='Phisical medicine', to_do='something do3')
    hospital_3 = Hospital(name='Nurcing department', to_do='something do2')

    database.session.add(admin1)
    database.session.add(admin2)

    database.session.add(hospital_1)
    database.session.add(hospital_2)
    database.session.add(hospital_3)

    database.session.add(employee_1)
    database.session.add(employee_2)
    database.session.add(employee_3)

    database.session.commit()
    database.session.close()


if __name__ == '__main__':
    try:
        populate_database()
    except Exception as e:
        print('An error occured while inserting data. Errortype: ' + str(e))
