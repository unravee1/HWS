from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import Plants
from app.forms import PlantsForm


plants_blueprint = Blueprint("plants", __name__)


@plants_blueprint.route("/add-plants", methods = ["GET", "POST"])
def add_plants():
    form = PlantsForm(request.form)
    if form.validate_on_submit():
        plant = Plants(
            title=form.title.data,
            location=form.location.data,
        )
        plant.save()
        flash("You added a new plant", "success")
        return redirect(url_for("main.plants"))
    elif form.is_submitted():
        flash("The given data was invalid.", "danger")
    return render_template("plants/register.html", form = form)