"""
This module represents the logic of authentication of user
"""
from flask import render_template, session, make_response, request, flash, redirect, url_for
from flask_login import login_required
from . import user
from ..service.admin import get_avatar, get_admin_by_name, update_avatar, check_if_is_available


@user.route('/profile')
@login_required
def profile():
    """
    Handle requests to the /profile route
    """
    admin_profile = get_admin_by_name(session['admin'])
    return render_template('profile.html', admin_profile=admin_profile)


@user.route('/avatar')
@login_required
def avatar():
    response = make_response(get_avatar(session['admin']))
    response.headers['Content-Type'] = 'image/png'
    return response


@user.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and check_if_is_available(file.filename):
            try:
                img = file.read()
                res = update_avatar(img, session['admin'])
                if not res:
                    flash("An error occured while updating avatar. Please try again", "error")
                flash("Avatar is changed successfully", "success")
            except FileNotFoundError as e:
                flash("An error occured. Please try again.", "error")
        else:
            flash("An error occured. This format file is not supported. Use png.", "error")

    return redirect(url_for('user.profile'))
