import email
from click import confirm
from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,email,equal_to
class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(),email()])
    password=PasswordField('password',validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in') 
    submit=SubmitField('Sign in')
class RegisterForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),length(min=4,max=20)])
    email=StringField('email',validators=[DataRequired(),email()])
    password=PasswordField('password',validators=[DataRequired(),equal_to('password')])
    confirm_password=PasswordField('Confirm password',validators=[DataRequired(),equal_to('password')])
    
    submit=SubmitField('Sign up')
    
