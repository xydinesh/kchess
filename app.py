from flask import Flask, request, render_template, redirect, url_for
import redis
import os
from datetime import datetime
from time import strftime
from pytz import timezone

redis_addr = os.environ.get('SERVER_PORT_6379_TCP_ADDR', 'localhost')
redis_port = os.environ.get('SERVER_PORT_6379_TCP_PORT', 6379)

r = redis.Redis(host=redis_addr, port=redis_port, db=3)
app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('summary'))

@app.route('/summary')
def summary():
    games = r.lrange('knoxville-games-list', 0, 100)
    print games
    return render_template('summary.html', games=list(games))

@app.route('/game/result', methods=['POST'])
def result():
    data = []
    fmt = "%Y-%m-%d %H:%M"
    now_time = datetime.now(timezone('US/Eastern'))
    data.append(now_time.strftime(fmt))
    data.append(request.form['white'])
    data.append(request.form['black'])
    data.append(request.form['result'])
    data.append(request.form['wtime'])
    data.append(request.form['btime'])
    data.append(request.form['comments'])
    st = '|'.join(data)
    r.rpush('knoxville-games-list', st)
    return "OK"

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
