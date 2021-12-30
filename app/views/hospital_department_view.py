"""
This module represents the logic on routes starting with /hospital
"""
from flask import render_template, redirect, flash, url_for, request, session
from flask_login import login_required, current_user

from . import user


@user.route('/departments', methods=["GET"])
def get_department_of_hospital():
    """
        This function renders the departments of hospital template
        on the /hospital route
    """
    return render_template('department_of_hospital/departments.html', session=current_user.is_authenticated)


@user.route('/departments/delete/<int:identifier>', methods=['GET'])
@login_required
def delete_department_of_hospital(identifier):
    """
    This function represents the logic on /hospital/delete address
    :return: the rendered departments.html template with deleted department if hospital
    """
    # redirect to departments.html after the element is deleted
    return redirect(url_for('user.get_department_of_hospital'))


@user.route('/departments/add', methods=['GET'])
@login_required
def add_department_of_hospital():
    """
    This function represents the logic on /hospital/add address
    :return: the rendered department.html template to add a new department  of hospital
    """
    if 'add' in str(request.url_rule):
        flag = True
    else:
        flag = False
    # load department.html template
    return render_template('department_of_hospital/department.html', flag=flag)


@user.route('/departments/edit/<int:identifier>', methods=['GET'])
@login_required
def edit_department_of_hospital(identifier):
    """
    This function represents the logic on /hospital/edit address
    :return: the rendered department.html template to edit an existing department of hospital
    """

    # load department.html template
    return render_template('department_of_hospital/department.html')
