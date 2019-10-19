from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from passlib.hash import pbkdf2_sha256
from login_model import User

#checking username and password
def invalid_credentials(form, field):
    password = field.data
    username = form.username.data

    #Checking username validity
    user.data = user.query.filter_by(username=username).first()
    if user_data is None:
        raise ValidationError("Login or password is incorrect")
    #Checking password validity
    elif not pbkdf2_sha256.verify(password, user_data.hashed_pswd):
        raise ValidationError("Login or password is incorrect")

class   RegistrationForm(FlaskForm):
    #Registration form
    username = StringField('username', validators=[InputRequired(message='Username required'), Length(min=3, max=20, message='Username should be between 3 and 20 characters.')])
    password = PasswordField('password', validators=[InputRequired(message='Password required'), Length(min=3, max=20, message='Password should be between 3 and 20 characters')])
    confirmpass = PasswordField('confirmpass', validators=[InputRequired(message='Password required'), EqualTo('password', message='Passwords should match')])

    def validateUsername(self, username):
        user_object = user.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError('The username chosen already exists. Please select a different username.')

class LoginForm(FlaskForm):
    #Forms to login
    username = StringField('username', validators=[InputRequired(message='Username required')])
    password = PasswordField('password', validators=[InputRequired(message='Password required'), invalid_credentials])
