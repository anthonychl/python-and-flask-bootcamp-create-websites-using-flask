import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #these environment variables are only needed when working locally 
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1' #no need for them when the app is deployed
#############################################################################################

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

blueprint = make_google_blueprint(client_id='855092671291-4jtfcv791qnbh5frlmpcv8iheva1k6e9.apps.googleusercontent.com',
                                    client_secret='7G0-XpWRBJ8Fwiv_KemJsBLL',
                                    offline=True, scope=['profile','email']) #offline is set to False by default, 'scope' (the information we want back) is a list with the profile name and email
app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # this view is demonstrative just to prove we cant skip ahead to this page, it should produce an error if not logged in
    resp = google.get('/oauth2/v2/userinfo') # grab a response
    assert resp.ok, resp.text # make sure the response was ok, it wasnt blank or empty, 
    email = resp.json()['email'] # the email of whoever logged in
    return render_template('welcome.html', email=email)
         
@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template('google.login')
    resp = google.get('/oauth2/v2/userinfo') # grab a response
    assert resp.ok, resp.text # make sure the response was ok, it wasnt blank or empty, 
    email = resp.json()['email'] # the email of whoever logged in
    return render_template('welcome.html', email=email)
                     
if __name__ == "__main__":
    app.run(debug=True)                                        