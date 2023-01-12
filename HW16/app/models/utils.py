from app import db


class ModelMixin(object):
    """ Add and save information in database.
    """
    def save(self):
        """ Add and save information in database.
        """
        db.session.add(self)
        db.session.commit()
        return self
