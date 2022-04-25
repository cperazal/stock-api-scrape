from .. import db

class Setup(db.Model):
    """ User Model for storing setup related details """
    __tablename__ = "setup"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    api_key = db.Column(db.String(300), unique=True, nullable=False)