from flask_sqlalchemy import SQLAlchemy
from app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), default='customer')
    signup_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
