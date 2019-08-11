from flask import Flask, render_template,flash,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KEY'

class SimpleForm(FlaskForm):
    breed = StringField('What breed is it?')
    submit = SubmitField('Click Me')


@app.route('/', methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('it is a :'+form.breed.data)
        return redirect(url_for('index'))
        
    return render_template('03-home.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)