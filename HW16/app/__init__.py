import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migration = Migrate()
mail = Mail()


def create_app(envoiroment="developement"):
    """ Create app, use configuration and registration blueprint. """
    from config import config
    from app.view import auth_blueprint, main_blueprint, plant_blueprint
    from app.models import User, AnonymousUser, Plant

    app = Flask(__name__)

    env = os.getenv("FLASK_ENV", envoiroment)
    app.config.from_object(config[env])
    config[env].configure(app)

    db.init_app(app)
    migration.init_app(app, db, compare_type=True)
    login_manager.init_app(app)

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(plant_blueprint)

    mail.init_app(app)

    @login_manager.user_loader
    def get_user(id):
        """ Getter information about user """
        return User.query.get(int(id))

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = AnonymousUser

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        """ Error handler. """
        return render_template("error.html", error=exc), exc.code

    return app
