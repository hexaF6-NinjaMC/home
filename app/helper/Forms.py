from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

class CreateUserForm(FlaskForm):
    name = StringField(label='Name: ', validators=[DataRequired()])
    email = EmailField(label='Email address: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)])
    password = PasswordField(label='Create password: ', validators=[DataRequired(), EqualTo(fieldname='password_confirmation', message='Passwords must match.')])
    password_confirmation = PasswordField(label='Confirm password: ', validators=[DataRequired(), EqualTo(fieldname='password', message='Passwords must match.')])
    submitBtn = SubmitField(label='Register')

class LoginForm(FlaskForm):
    email = EmailField(label='Email: ', validators=[DataRequired(), Email(message='Text in email field is not a valid format.', check_deliverability=True)])
    password = PasswordField(label='Password: ', validators=[DataRequired()])
    submitBtn = SubmitField(label='Submit')