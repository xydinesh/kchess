from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from time import strftime
from pytz import timezone
from datetime import datetime

from app import app

# postgresql://scott:tiger@localhost/mydatabase
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@192.168.59.103:5432/docker'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, name=None, email=None):
        self.username = username
        if name is not None:
            self.name = name

        if email is not None:
            self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_time = db.Column(db.DateTime)
    white_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    white = db.relationship('User',
        backref=db.backref('results', lazy='dynamic'))
    black_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    black = db.relationship('User',
        backref=db.backref('results', lazy='dynamic'))
    result = db.Column(db.Integer)
    wtime = db.Column(db.String(8))
    btime = db.Column(db.String(8))
    notes = db.Column(db.String(140))

    def __init__(self, white, black, result, wtime, btime, rec_time=None, notes=None):
        self.white = white
        self.black = black
        self.result = result
        self.wtime = wtime
        self.btime = btime
        if rec_time is None:
            rec_time = datetime.now(timezone('US/Eastern'))
        if notes is not None:
            self.notes = notes

    def __repr__(self):
        return '<Result %r %r %r>' % (self.white, self.black, self.result)