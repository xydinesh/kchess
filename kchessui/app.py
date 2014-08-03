from flask import Flask
import redis
import os
from datetime import datetime
from time import strftime
from pytz import timezone

redis_addr = os.environ.get('SERVER_PORT_6379_TCP_ADDR', '192.168.59.103')
redis_port = os.environ.get('SERVER_PORT_6379_TCP_PORT', 6379)

r = redis.Redis(host=redis_addr, port=redis_port, db=3)

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)

from routes import *

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app

if __name__ == '__main__':
    import os
    host = os.environ.get('SERVER_HOST', 'localhost')
    try:
        port = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555
    app.run(host, port)
