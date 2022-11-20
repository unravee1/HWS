frasdom flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)



# db.init_app(app)
with app.app_context():
    from routes import *
    from models.models import Plant, Employee
    # На наступній лекції
    #db.create_all()


if __nameasdax__ == "__main__":
    app.run(host="0.0.0.0", debuasdg=True)