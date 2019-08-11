from user import User

users  = [User(1,'Anthony','pass'), User(2, 'Dela', 'pass2')]

username_table = {u.username: u for u in users} #dictionary comprehension, mapping the user object to the user's username

userid_table = {u.id: u for u in users} # the same, this time mapping the object to it's id

def authenticate(username, password):
    #check if user exists, and return it if so
    user = username_table.get(username,None) # 'None' is another option to return, if the username isnt found return 'None'
    if user and password == user.password:
        return user

def identity(payload): # check the Flask-JWT documentation
    user_id = payload['identity']
    return userid_table.get(user_id,None)

