from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy</h1>"

@app.route('/information')
def info():
    return "Puppies are cute"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {} </h1>".format(name.upper())


if __name__ == "__main__":
    app.run()