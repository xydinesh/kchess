import redis
import os
from datetime import datetime
from time import strftime
from pytz import timezone
from datetime import datetime
from flask import request, render_template, redirect, url_for
from app import app

redis_addr = os.environ.get('SERVER_PORT_6379_TCP_ADDR', '192.168.59.103')
redis_port = os.environ.get('SERVER_PORT_6379_TCP_PORT', 6379)

r = redis.Redis(host=redis_addr, port=redis_port, db=3)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Your contact page.'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title = 'About',
        year = datetime.now().year,
        message = 'Your application description page.'
    )

@app.route('/summary')
def summary():
    games = r.lrange('knoxville-games-list', 0, 100)
    return render_template('summary.html', games=list(games))

@app.route('/game/result', methods=['POST'])
def result():
    print request.form
    data = []
    fmt = "%Y-%m-%d %H:%M"
    now_time = datetime.now(timezone('US/Eastern'))
    data.append(now_time.strftime(fmt))
    data.append(request.form['white'])
    data.append(request.form['black'])
    data.append(request.form['result'])
    data.append(request.form['wtime'])
    data.append(request.form['btime'])
    # data.append(request.form['comments'])
    st = '|'.join(data)
    r.rpush('knoxville-games-list', st) 
    print st
    return redirect(url_for('home'), code=302)

@app.route('/report')
def report():
    return render_template('report.html')