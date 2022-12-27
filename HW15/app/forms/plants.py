from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class PlantsForm(FlaskForm):
    title = StringField("Title")
    location = StringField("Location")
    submit = SubmitField("Save")