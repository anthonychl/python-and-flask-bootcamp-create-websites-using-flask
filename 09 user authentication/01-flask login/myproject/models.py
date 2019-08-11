from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # UserMixin class gives us access to attributes we'll use later

@login_manager.user_loader #this decorator and function below ,allow flask-login to load the current user and grab their ID, so once someone is logged in we can show pages specific to their login id
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(64), unique=True, index= True) #db.String(64) setting max length of the string, Setting the email to be Unique(users cant share same email)
    username = db.Column(db.String(64), unique=True, index= True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password) 
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)