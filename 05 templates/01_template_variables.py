from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name='anthony'
    letters = list(name)
    pup_dictionary = {'pup_name':'max'}
    return render_template("01-Template-Variables.html",name=name,mylist=letters,mydict=pup_dictionary)



if __name__ == "__main__":
    app.run(debug=True)