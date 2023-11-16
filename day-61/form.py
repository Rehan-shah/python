
import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField , SubmitField
from wtforms.validators import DataRequired ,Email, Length

class SignUpForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() , Email() , Length(min=6 , max=120)]) 
    password = PasswordField('Password' , validators=[DataRequired() , Length(min=8)])
    login_btn = SubmitField('Login') 
