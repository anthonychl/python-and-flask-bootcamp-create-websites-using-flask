import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.Integer)
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic' ) # One to Many relationship, a pup can have many toys
    owner = db.relationship('Owner', backref='puppy', uselist=False) #One to one, a pup can only have one owner
            #the first parameter is the name of the model: Toy, Owner
            #backref: reference in the other model back to puppy
            #lazy: specifies how the related items are to be loaded, there are options like 'select','immediate'...
            #uselist: is set to True by default, set False on a one to one relationship

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"The pup name is {self.name} and it's owner is: {self.owner.name}"
        else:
            return f"The pup name is {self.name} and has no owner"
    
    def report_toys(self):
        print("here are my toys:")
        for toy in self.toys:
            print(toy.item_name)



class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id
