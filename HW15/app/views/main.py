from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import Plants


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return render_template("index.html")


@main_blueprint.route("/about")
def about():
    return render_template("about.html")


@main_blueprint.route("/plants")
def plants():
    all_plants = Plants.query.all()
    return render_template("plants/profile.html", all_plants=all_plants)

