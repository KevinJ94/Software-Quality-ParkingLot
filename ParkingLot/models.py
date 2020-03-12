# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Billing(db.Model):
    __tablename__ = 'billing'

    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float(255))
    createTime = db.Column(db.DateTime)
    finishTime = db.Column(db.DateTime)
    status = db.Column(db.String(255))
    description = db.Column(db.String(255))
    userId = db.Column(db.ForeignKey('user.id'), index=True)
    year = db.Column(db.String(255))
    month = db.Column(db.String(255))
    user = db.relationship('User', primaryjoin='Billing.userId == User.id', backref='billings')


class Plate(db.Model):
    __tablename__ = 'plate'

    id = db.Column(db.Integer, primary_key=True)
    plateNumber = db.Column(db.String(255))
    registrationNumber = db.Column(db.String(255))
    userId = db.Column(db.Integer)


class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    birthday = db.Column(db.DateTime)
    userId = db.Column(db.ForeignKey('user.id'), index=True)

    user = db.relationship('User', primaryjoin='Profile.userId == User.id', backref='profiles')


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255))
    type = db.Column(db.String(255))
    confirmNum = db.Column(db.Integer)
    userId = db.Column(db.ForeignKey('user.id'), index=True)
    startTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)

    user = db.relationship('User', primaryjoin='Reservation.userId == User.id', backref='reservations')


class Spot(db.Model):
    __tablename__ = 'spot'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(255))
    status = db.Column(db.String(255))
    current = db.Column(db.Integer)


class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(255))
    createTime = db.Column(db.DateTime)
    endTime = db.Column(db.DateTime)
    expectedDuration = db.Column(db.String(255))
    userId = db.Column(db.ForeignKey('user.id'), index=True)
    user = db.relationship('User', primaryjoin='Transaction.userId == User.id', backref='transactions')


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255))
    isArrive = db.Column(db.Integer)


class Home():
    user_number = 0
    free_spot = 0
    reserved_spot = 0
    occupied_spot = 0


