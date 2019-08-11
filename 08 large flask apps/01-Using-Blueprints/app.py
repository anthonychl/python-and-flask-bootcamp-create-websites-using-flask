# This is app.py, this is the main file called <-- this means we run this file to run the app
from myproject import app #this means: from __init__.py import app <--DONT code it like it's commented
from flask import render_template



@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
