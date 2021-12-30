"""
This module creates WTForm to provide security of authentication

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    This class create WTForm to login admin user. There are four fields to enter data

    """
    username = StringField('Admin\'s username: ', validators=[DataRequired(),
                                                              Length(min=4, max=25,
                                                                     message='Field must be between 4 and 100 characters long.')])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=4, max=100)])
    submit = SubmitField('Enter')
