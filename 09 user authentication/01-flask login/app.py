from myproject import app,db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required #makes sure the user is logged in to be able to see this VIEW
def welcome_user():
    return render_template('welcome.html')

@app.route("/logout")
@login_required
def logout():
    logout_user() #logs the user out for us
    flash("you logged out!")
    return redirect(url_for('home'))

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user.check_password(form.password.data) and user is not None: #if the password matches, and the user exists
            login_user(user) # the function logs in the user for us
            flash('logged in successfully')
            # if the user was trying to get to a certain page that needed logging in
            # and was redirected to the login form,
            # that page gets saved in request.args.get('next'), 
            # and after logging in the user will be redirected to it
            # if the user entered directly to the login form, then it will be redirected to the 'welcome_user' page
            next = request.args.get('next') 
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')
            return redirect(next)
        
    return render_template('login.html', form=form) 

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data,)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering!')
        return redirect(url_for('login'))
    return render_template('register.html', form= form)

if __name__ == "__main__":
    app.run(debug= True)




