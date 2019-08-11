from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('00-Basic-Template.html')

if __name__ == "__main__":
    app.run(debug=True)