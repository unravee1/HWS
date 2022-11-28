from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

app = Flask(__name__)
app.config.from_object("config.Config")
app.secret_key = "secret123"
db = SQLAlchemy()

db.init_app(app)


migrate = Migrate(app, db)

api = Api(app)

with app.app_context():
    from routes import *
    from models.models import *
    from routes.api.employee import *
    from routes.api.plant import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)