from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)




with app.app_context():
    from routes import *
    from models.models import Plant, Employee


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)