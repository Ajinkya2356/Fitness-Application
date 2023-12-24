from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    First_name = db.Column(db.String(150), nullable=False)
    role=db.Column(db.String(10),nullable=False)


class UserInformation(db.Model, UserMixin):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True, primary_key=True)
    user = db.relationship('User', backref=db.backref('user_information', lazy=True))
    First_Name = db.Column(db.String(30), nullable=False)
    Last_Name = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Mobile=db.Column(db.Integer,unique=True,nullable=False)
    Address = db.Column(db.String(120), nullable=True)
    Postcode = db.Column(db.Integer, nullable=True)
    Weight = db.Column(db.Integer, nullable=False)
    Height = db.Column(db.Integer, nullable=False)
    M_calories = db.Column(db.Integer, nullable=False)
    Intensity = db.Column(db.String(10), nullable=True)
   


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150), nullable=False)
    Email = db.Column(db.String(20), nullable=False)
    Message = db.Column(db.String(1000), nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)