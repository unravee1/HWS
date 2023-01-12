from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    """ Login form accepts email or username and password user.
    """
    user_identifier = StringField("Username or Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class RegistrationForm(FlaskForm):
    """ Registration form accepts information about user such as: name, username, email, password.
    """
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired(), Length(8, 255)])
    password_confirmation = PasswordField("Confirm Password", [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(form, field):
        """ Validation username. Search username in tables users our database.
            If our database has this user raises ValidationError and input message obout it.
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("This username is taken.")

    def validate_email(form, field):
        """ Validation email. Search email in tables users our database.
            If our database has user with this email raises ValidationError and input message about it.
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("This email is already registered.")


class ProfileForm(FlaskForm):
    """ Profile form accepts information about user such as: name, username, email, password.
    """
    first_name = StringField("First name")
    last_name = StringField("Last name")
    username = StringField("Username", [DataRequired(), Length(4, 255)])
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Register")


class ForgotPasswordForm(FlaskForm):
    """ Forgot password form accepts information about email users.
    """
    email = StringField("Email Address", [DataRequired(), Email()])
    submit = SubmitField("Reset Password")

    def validate_email(form, field):
        """ Validation email in forgot password form. Search email in tables users our database.
            If our database don't have user with this email raises ValidationError and input message about it.
        """
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError("Not found registered user with this email.")


class PasswordResetForm(FlaskForm):
    """ Password reset form accepts information about new password user and confirmation it.
    """
    password = PasswordField("Password", [DataRequired(), Length(8, 255)])
    password_confirmation = PasswordField("Confirm Password", [DataRequired(), EqualTo("password")])
    submit = SubmitField("Save")
