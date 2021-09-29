from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# I am setting the limits for when the user is typing their information - like forcing their email to be unique  by using FLASK SQL ALCHEMY 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
