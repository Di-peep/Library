"""
This module represents the logic of authentication of user
"""
from flask import render_template, redirect, flash, session, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from . import user
from . import WTForm
from ..models.admin import Admin
from werkzeug.security import check_password_hash
from app import login_manager
from app.service.admin import get_admin_by_name


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


@user.route('/login', methods=["POST", "GET"])
def login():
    """
    Handle requests to the /login route
    Cretates login page using WTForm using post-requests.
    Admin data contains in MySQL database

    :return: html page
    """
    session.permanent = True
    if current_user.is_authenticated:
        flash('You are already authorized', 'success')
        return redirect(url_for('user.home_page'))
    form = WTForm.LoginForm()
    if form.validate_on_submit():
        root_user = get_admin_by_name(form.username.data)
        if not root_user:
            flash('An error occured. Try to enter correct name of password', 'error')
            return redirect(url_for('user.login'))
        if not check_password_hash(root_user.password, form.password.data):
            flash('An error occured. Try to enter correct name of password', 'error')
            return redirect(url_for('user.login'))
        login_user(root_user)
        session['admin'] = root_user.username
        return redirect(url_for('user.home_page'))
    return render_template('login.html', form=form)


@user.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Allow employee to logout moving to home page.
    """
    logout_user()
    return redirect(request.referrer)
