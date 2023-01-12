from flask import render_template

from app import app

@app.route('/calc/<int:first_number>/<int:second_number>')
def calc(first_number, second_number):
    return str(first_number + second_number)