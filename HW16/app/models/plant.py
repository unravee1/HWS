from app import db
from app.models.utils import ModelMixin


class Plant(db.Model, ModelMixin):
    """ Model plant. Uses for create table 'plants' in database.
    """
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=True)
