import os

from datetime import datetime

from flask import request, render_template, redirect, url_for
from kchessui.models import *
from kchessui import app, db, login_manager

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


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
    results = Result.query.all()
    return render_template('summary.html', games=results, year = datetime.now().year)

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

    user = User.query.filter_by(username=request.form.get('white')).first()
    if user is None:
        db.session.add(User(username=request.form.get('white')))
        db.session.commit()

    # data.append(request.form['comments'])
    st = '|'.join(data)
    print st
    return redirect(url_for('home'), code=302)

@app.route('/report')
def report():
    return render_template('report.html', 
                           year = datetime.now().year)

@app.route('/user/signup', methods=['POST'])
def user_signup():
    username = request.form.get('username')
    email = request.form.get('email')
    name = request.form.get('name')
    print username, email, name
    return redirect(url_for('home'), code=302)
    

@app.route('/signup')
def signup():
    return render_template('signup.html',                          
                           year = datetime.now().year)