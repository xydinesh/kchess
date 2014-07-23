from flask import Flask, request, render_template
import redis
from datetime import datetime
from time import strftime
from pytz import timezone
r = redis.Redis(host='localhost', port=6379, db=3)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Index Page'

@app.route('/summary')
def hello():
    games = r.smembers('knoxville-games')
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
    r.sadd('knoxville-games', st)
    return "OK"

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0', port=8080)
