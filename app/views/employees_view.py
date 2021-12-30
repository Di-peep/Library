"""
This module represents the logic on routes starting with /employees
"""
from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required

from . import user


@user.route('/employees', methods=["POST", "GET"])
def get_employees():
    return render_template('employees_of_hospital/employees.html')


@user.route('/employees/delete/<int:identifier>', methods=['GET', 'POST'])
def delete_employee(identifier):
    """
    This function represents the logic on /employees/delete address
    :return: the rendered employees.html template with deleted employee
    """
    # form a flash message
    flash('You have successfully deleted the employee.')

    # redirect to employees.html after the element is deleted
    return redirect(url_for('user.get_employees'))


@user.route('/employees/add', methods=['GET'])
@login_required
def add_employee():
    """
    This function represents the logic on /employees/add address
    :return: the rendered employee.html template to add a new employee
    """
    # declare a flag variable which indicates which title to load 'Add' or 'Edit' at employee.html
    if 'add' in str(request.url_rule):
        flag = True
    else:
        flag = False
    # load employee.html template
    return render_template('employees_of_hospital/employee.html', flag=flag)


@user.route('/employees/edit/<int:identifier>', methods=['GET'])
@login_required
def edit_employee(identifier):
    """
    This function represents the logic on /employees/edit address
    :return: the rendered employee.html template to edit an existing employee
    """

    # load employee.html template
    return render_template('employees_of_hospital/employee.html')
