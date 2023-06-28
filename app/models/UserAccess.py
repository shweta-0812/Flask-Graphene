from datetime import datetime as dt
from flask import current_app as app

from app import db


class UserAccess(db.Model):
    __tablename__ = "UserAccess"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_active = db.Column(db.Integer, nullable=False, default=1)
    is_verified = db.Column(db.Integer, nullable=False, default=0)
    is_admin = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=dt.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, user_id):
        self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def set active/verified/admin
