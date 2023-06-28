from datetime import datetime as dt
from crypt import crypt
from flask import current_app as app

from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    last_logged_in = db.Column(db.DateTime, default=dt.now())
    created_at = db.Column(db.DateTime, default=dt.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, client_id, username, email, password):
        def _hashed_password(plain_password):
            return crypt.generate_password_hash(plain_password)

        self.client_id = client_id
        self.username = username
        self.email = email
        self.password = _hashed_password(password)

    def save(self):
        """ Shorthand method to update User object """
        db.session.add(self)
        db.session.commit()
