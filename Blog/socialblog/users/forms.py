from ast import Sub
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileAllowed,FileField

from flask_login import current_user
from socialblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Your email has been already registered')

    def check_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Your username has been already registered!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed('jpg','png')])
    submit = SubmitField('Update')

    def check_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email=self.email.data).first():
                raise ValidationError('Your email has been already registered')

    def check_username(self,username):
        if username.data != current_user.username:
            if User.query.filter_by(username=self.username.data).first():
                raise ValidationError('Your username has been already registered!')