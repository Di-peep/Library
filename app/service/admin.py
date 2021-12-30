"""
This module defines crud operations to work with admin table
"""
from flask import url_for

from app.models.admin import Admin
from app import database, create_app


def get_admin_by_name(username: str):
    """
    This function is used to get the single admin by id
    :param username: the username of the admin to get
    :return: the admin  with the specified username
    """
    admin = Admin.query.filter_by(username=username).first()
    return admin if admin is not None else None


def get_all_admin() -> str:
    """
    This function is used to get the single admin by id
    :return: the admin  with the specified username
    """
    admin = Admin.query.all()
    return admin if admin is not None else None


def get_avatar(username: str):
    """
    This function get admin avatar
    :return: avatar of admin account
    """
    admin = Admin.query.filter_by(username=username).first()
    if not admin.avatar:
        with create_app().open_resource(create_app().root_path + url_for('static', filename='images/default.png'),
                                        "rb") as img:
            avatar = img.read()
    else:
        avatar = admin.avatar
    return avatar


def update_avatar(avatar, username: str) -> bool:
    """
    This bodule updates admin's avatar
    :param avatar: file
    :param username: str
    :return: bool
    """
    if not avatar:
        return False
    try:
        admin = Admin.query.filter_by(username=username).first()
        admin.avatar = avatar
        database.session.add(admin)
        database.session.commit()
    except Exception:
        return False
    return True


def check_if_is_available(filename) -> bool:
    """
    this module checks if format of file is available
    :param filename: file
    :return: bool
    """
    file = filename.rsplit('.', 1)[1]
    if file == "png" or file == "PNG":
        return True
    return False
