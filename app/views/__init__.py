"""
__init__.py file of views module with
imported info, employee_view and department_view submodules
Register the user blueprint and specify the logic on '/' and '/home' addresses
Also handle an error status
"""

# pylint: disable=cyclic-import
from flask import Blueprint
from flask import render_template, session

user = Blueprint('user', __name__)
from . import authentification_view
from . import hospital_department_view
from . import employees_view
from . import profile_view

# because the blueprint must be registered before importing the views


@user.route('/')
@user.route('/home')
def home_page():
    """
    Render the home page template on the / route
    """
    return render_template('index.html', session=session)


@user.app_errorhandler(404)
def handle_404(err):
    """
    Handel 404 error and redirect to 404.html page
    """
    return render_template('404.html'), 404


@user.app_errorhandler(401)
def handle_401(err):
    """
    Handel 401 error and redirect to 401.html page
    """
    return render_template('401.html'), 401
