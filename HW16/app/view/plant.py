from flask import Blueprint, request, flash, redirect, url_for, render_template
from app.forms.plant import RegistrationForm, ProfileForm
from app.models.plant import Plant

plant_blueprint = Blueprint("plant", __name__)


@plant_blueprint.route("/plant/register", methods=["GET", "POST"])
def register():
    """ Register plant route. Input request from web page. Validates this request form.
        Use a form to validate and save plant in database.
    """
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        plant = Plant(
            title=form.title.data,
            location=form.location.data,
        )
        plant.save()
        flash("Registration plant is successful.", "success")
        return redirect(url_for("main.index"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("plant/register.html", form=form)


@plant_blueprint.route("/plant/profile_all", methods=["GET", "POST"])
def profile_all():
    """ Profile all plants route. Input request from web page. Validates this request form.
       Use from output information about plants.
    """
    plants: Plant = Plant.query.all()
    form = ProfileForm()
    return render_template("plant/profile.html", form=form, plants=plants)
