from flask import render_template, flash, redirect, request, Blueprint, url_for
from flask_login import login_user, current_user, logout_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

#register
@users.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('users.login'))
    return render_template('register.html', form = form)

#login
@users.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in success')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form = form)

#logout
@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#account
@users.route('/account', methods = ['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data, username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account updated')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static', filename = 'profile_pics/'+current_user.profile_image)
    return render_template('account.html', profile_image = profile_image,form = form)

#list of user's Blog posts
@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page', 1, type = int) # will allow us (along with some other stuff) to cycle through posts via different pages, ie assume a user has a 100 posts, they wont all be shown in one page 
    user = User.query.filter_by(username = username).first_or_404() # grab the first user of that name or throw an error page ie if the user doesnt exist
    blog_posts = BlogPost.query.filter_by(author = user).order_by(BlogPost.date.desc()).paginate(page = page, per_page = 5) # paginate() actually allow us to have those pages to cycle through
    return render_template('user_blog_posts.html', blog_posts = blog_posts, user = user)

