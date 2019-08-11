import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate


###### CREATING A SQLite DATABASE ###########

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite') #setting the location and name of the database 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turning off the feature to track modifications, we dont need this right now :)

db = SQLAlchemy(app)

Migrate(app, db)

##############################################

###### CREATE A MODEL ##################

class Puppy(db.Model):
    __tablename__ = 'puppies' 

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f"The puppy name is: {self.name} and it is: {self.age} years old"
        
##################################################



