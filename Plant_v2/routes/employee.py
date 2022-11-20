from app import app, db
from flask import render_template, request, redirect
from models.models import Plant


@app.route("/add-employee", methods=["POST", "GET"])
def add_employee():
        plants = Plant.query.all()
        return render_template("add_employee.html", plants=plants)