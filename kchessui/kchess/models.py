from flask import Flask
from kchess import db

from time import strftime
from pytz import timezone
from datetime import datetime

from passlib.context import CryptContext
crypt_ctx = CryptContext(schemes=["sha256_crypt"])

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)
    hash_password = db.Column(db.String(128))    
    def __init__(self, username, password, name=None, email=None):
        self.username = username
        self.hash_password = crypt_ctx.encrypt(password)
        if name is not None:
            self.name = name

        if email is not None:
            self.email = email
    
    # adding verify method to use with passlib
    def  verify_password(self, password):
        return crypt_ctx.verify(password, self.hash_password)

    def set_password(self, password):
        self.hash_password = crypt_ctx.encrypt(password)

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    rec_time = db.Column(db.DateTime)
    result = db.Column(db.String(16))
    wtime = db.Column(db.String(128))
    btime = db.Column(db.String(128))
    notes = db.Column(db.String(140))
    white = db.Column(db.String(128), db.ForeignKey('users.username'))
    black = db.Column(db.String(128), db.ForeignKey('users.username'))
    white_player = db.relationship("User", primaryjoin="Result.white==User.username")
    black_player = db.relationship("User", primaryjoin="Result.black==User.username")

    def __init__(self, white, black, result, wtime=None, btime=None, notes=None):
        self.white = white
        self.black = black
        self.result = result
        self.wtime = wtime
        self.notes = notes
        if wtime is None:
            self.wtime = '0:00'

        self.btime = btime
        if btime is None:
            self.btime = '0:00'
      
        fmt = "%Y-%m-%d %H:%M"
        now_time = datetime.now(timezone('US/Eastern'))
        self.rec_time = now_time.strftime(fmt)         

    def __repr__(self):
        return '<Result %r %r %r>' % (self.white, self.black, self.result)