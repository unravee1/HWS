from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from app.models import Plant


class RegistrationForm(FlaskForm):
    """ Registration form accepts information about plant such as: title and location.
    """
    title = StringField("Title")
    location = StringField("Location")
    submit = SubmitField("Register")

    def validate_title(form, field):
        """ Plant title validation. Search plant with this title in tables plants our database.
            If our database has plant with this title raises ValidationError and input message obout it.
        """
        if Plant.query.filter_by(title=field.data).first():
            raise ValidationError("This username is taken.")


class ProfileForm(FlaskForm):
    """ Profile form accepts information about plant such as: title and location.
    """
    title = StringField("Title")
    location = StringField("Location")
    submit = SubmitField("Register")
