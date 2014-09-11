from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, logout_user, current_user

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xydinesh:docker@127.0.0.1:5432/kchess'
app.config['SECRET_KEY'] ='xxxxxxxx arseintaorsnetia astaorsitnarosetni'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app

from kchess.routes import *
from kchess.models import *



