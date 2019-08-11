import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

###### CREATING A SQLite DATABASE ###########

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ ==> basicModelApp.py
# os.path.dirname(__file__) ==> /00 Model and CRUD basics/
# os.path.abspath(os.path.dirname(__file__)) ==> E://Auto../.../00 Model and CRUD basics/

# os.path saves us time not having to look for the directory ourselves and it works for any OS

app = Flask(__name__)

# this connects our flask app to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite') #setting the location and name of the database 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turning off the feature to track modifications, we dont need this right now :)

db = SQLAlchemy(app)

##############################################

###### CREATE A MODEL ##################

class Puppy(db.Model):
    __tablename__ = 'puppies' #overwrite table name

    #creating columns for the table
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        #note the id will be generated for us automatically later
        self.name = name
        self.age = age
    
    def __repr__(self):
        # this is the string representation of a puppy in the model
        return f"The puppy name is: {self.name} and it is: {self.age} years old"
        
##################################################



