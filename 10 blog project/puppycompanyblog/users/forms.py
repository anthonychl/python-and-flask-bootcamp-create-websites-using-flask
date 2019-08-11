from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed # this will let us update  *.jpeg or *.png files for our profile pics

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()] )
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()] )
    username = StringField('UserName', validators =[DataRequired()] )
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', message = 'passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your email has been registered already")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your user name is taken")

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()] )
    username = StringField('UserName', validators =[DataRequired()] )
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("That email has been registered already")

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError("That user name is taken")

