from flask import render_template, Blueprint

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    """ Route start pages. Render index.html """
    return render_template("index.html")


@main_blueprint.route("/about")
def about():
    """ Route about pages. Render about.html """
    return render_template("about.html")


@main_blueprint.route("/plant")
def plants():
    """ Route start pages. Render plants.html """
    return render_template("plants.html")
