# Create, Update and Delete Users
# Profile Image Handler

# For the forms itself
from flask_wtf import FlaskForm

# Form structure and validators
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

# This is used for the profile images
from flask_wtf.file import FileField, FileAllowed

# Handles users
from flask_login import current_user
from blog.models import User

class LoginForm(FlaskForm):
    email = StringField('E-mail: ', validators=[DataRequired('This field cannot be empty.'), Email('Please provide an actual e-mail address')])
    password = PasswordField('Password: ', validators=[DataRequired('This field cannot be empty.')])
    submit = SubmitField('Log-In')

class RegisterForm(FlaskForm):
    email = StringField('E-mail: ', validators=[DataRequired('This field cannot be empty.'), Email('Please provide an actual e-mail address')])
    username = StringField('Username: ', validators=[DataRequired('This field cannot be empty.')])
    password = PasswordField('Password: ', validators=[DataRequired('This field cannot be empty.'), EqualTo('password_confirm', message='Password is not the same.')])
    password_confirm = PasswordField('Confirm Password: ', validators=[DataRequired('This field cannot be empty.')])
    submit = SubmitField('Register')

    # Prevents the same e-mail to be registered
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('E-mail already registered.')

    # Prevents the same username to be registered
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered.')

class UpdateUserForm(FlaskForm):
    email = StringField('E-mail: ', validators=[DataRequired('This field cannot be empty.'), Email('Please provide an actual e-mail address')])
    username = StringField('Username: ', validators=[DataRequired('This field cannot be empty.')])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Update')


