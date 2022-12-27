from app import db
from app.models.utils import ModelMixin


class Plants(db.Model, ModelMixin):

    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.title