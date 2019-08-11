from flask import Flask, render_template, session, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,DateTimeField,
                     BooleanField,TextAreaField,TextField,
                     RadioField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MYSECRETKEY'

class InfoForm(FlaskForm):
    breed = StringField('What breed is it?', validators=[DataRequired()])
    neutered = BooleanField('Has it been neutered?')
    mood = RadioField("Select your mood:",choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u"Pick your fav food: ",choices=[('ch','Chicken'),('bf','Beef'),('fi','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou')) 
    
    return render_template('01-Home.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('01-thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)
