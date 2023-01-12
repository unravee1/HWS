from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.models.user import User
from app.forms.auth import LoginForm, RegistrationForm, ProfileForm, ForgotPasswordForm, PasswordResetForm
from app import mail
from sqlalchemy import func
from flask_mail import Message

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """ Login user route. Input request from web page. Validates this request form.
        Use a custom Login Form to validate.
    """
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.authenticate(form.user_identifier.data, form.password.data)
        if user:
            login_user(user)
            flash("login successful.", "success")
            return redirect(url_for("main.index"))
        flash("Wrong username or password.", "danger")
    return render_template("auth/login.html", form=form)


@auth_blueprint.route("/loguot", methods=["GET"])
def logout():
    """ Logout user route. Input request from web page.
        Use a custom Logout Form to close session.
    """
    logout_user()
    flash("Logout successful.", "success")
    return redirect(url_for("main.index"))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    """ Register user route. Input request from web page. Validates this request form.
        Use a custom Login Form to validate and save user in database.
    """
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        user.save()
        login_user(user)
        flash("Registration successful. Your logged in.", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("auth/register.html", form=form)


@auth_blueprint.route("/profile", methods=["GET", "POST"])
def profile():
    """ Profile user route. Input request from web page. Validates this request form.
        Use from output information about user and change it.
    """
    user: User = User.query.get(current_user.id)
    form = ProfileForm()
    if form.validate_on_submit():
        user.first_name = form.first_name.data,
        user.last_name = form.last_name.data,
        user.username = form.username.data,
        user.email = form.email.data,
        user.save()

        flash("Profile has been successfully updated", "info")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    elif request.method == "GET":
        form.first_name.data = user.first_name
        form.last_name.data = user.last_name
        form.username.data = user.username
        form.email.data = user.email
    return render_template("auth/profile.html", form=form)


@auth_blueprint.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    """ Reset password user route. Input request from web page. Validates this request form.
        If user email has in our database password this user change on new password.
    """
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user: User = User.query.filter(func.lower(User.email) == func.lower(form.email.data)).first()
        if user:
            user.reset_password()
            print(url_for("auth.forgot_password", reset_password_uuid=user.reset_password_uuid, _external=True))
            email_message = Message('Hello', sender='sendler@mail.com', recipients=[str(form.email.data)])
            email_message.body = "From change password your account, follow this link:\n\n" + str(
                url_for("auth.forgot_password",
                        reset_password_uuid=user.reset_password_uuid,
                        _external=True)) + "\n\nIf you don't want to change password your account, ignore this message!"
            mail.send(email_message)
            flash("A link to change your password has been sent to the email address.", "success")
            return redirect(url_for("main.index"))
        flash("User not found.", "danger")
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("auth/reset_password.html", form=form)


@auth_blueprint.route("/forgot_password/<reset_password_uuid>", methods=["GET", "POST"])
def forgot_password(reset_password_uuid: str):
    """ Forgot password user route. Input request from web page. Validates this request form.
        If user email has in our database password this user change on new password.
    """
    user: User = User.query.filter(User.reset_password_uuid == reset_password_uuid).first()
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("main.index"))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user.password = form.password.data
        user.reset_password_uuid = ""
        user.save()
        login_user(user)
        flash("Login successful.", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("auth/forgot_password.html", form=form, reset_password_uuid=reset_password_uuid)
