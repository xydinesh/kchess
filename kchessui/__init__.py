from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@192.168.59.103:5432/docker'
app.config['SECRET_KEY'] ='xxxxxxxxarseintaorsnetia astaorsitnarosetni'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app


from kchessui.routes import *
from kchessui.models import *


