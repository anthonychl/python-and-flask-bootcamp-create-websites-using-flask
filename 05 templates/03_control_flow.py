from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mylist = ['Max','Rufus','Spot']
    return render_template("03-Template-Control-Flow.html",puppies=mylist)



if __name__ == "__main__":
    app.run(debug=True)