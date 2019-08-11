from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name="Max"
    return render_template("02-Template-Filters.html",name=name)



if __name__ == "__main__":
    app.run(debug=True)