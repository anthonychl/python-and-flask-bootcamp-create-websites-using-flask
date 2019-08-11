from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):
    id = IntegerField('Id of the puppy to remove: ')
    submit = SubmitField('Remove puppy')

class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner: ')
    puppy_id = IntegerField('Id of the puppy owned: ')
    submit = SubmitField('Add owner')
