from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class ContactForm(FlaskForm):
    username = StringField('EMAIL', validators=[InputRequired(), Length(min=5, max=100)])
    query = TextAreaField('ASK ANQI', validators=[InputRequired(), Length(max=500)])
    submit = SubmitField('Submit')