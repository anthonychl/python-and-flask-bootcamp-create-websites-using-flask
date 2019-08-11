# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return "<h1> Hello go to /puppy_latin/type_a_dog_name_here </h1>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    if name[-1] == 'y':
        return "<h1> {} in puppy-latin is: {}".format(name, name[:-1])+"iful"
    else:
        return "<h1> {} in puppy-latin is: {}".format(name, name)+"y"
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    

if __name__ == '__main__':
    app.run(debug=True)
