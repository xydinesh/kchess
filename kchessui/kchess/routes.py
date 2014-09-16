import os

from datetime import datetime

from flask import request, render_template, redirect, url_for, flash, g
from kchess.models import *
from kchess import *

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )

@app.route('/summary')
@login_required
def summary():
    results = Result.query.all()
    return render_template('summary.html', games=results, year = datetime.now().year)

@app.route('/game/result', methods=['POST'])
@login_required
def result():
    print request.form
    white = request.form.get('white')
    if white is None:
        raise Exception('White player name missing')

    black = request.form.get('black')
    if black is None:
        raise BaseException('Black player name missing')

    result = request.form.get('result')
    if result is None:
        raise Exception('Invalid result')

    wtime = request.form.get('wtime')
    btime = request.form.get('btime')
    notes = request.form.get('notes')
    
    result = Result(white=white, black=black, result=result, wtime=wtime, btime=btime, notes=notes)
    if result is not None:
        db.session.add(result)
        db.session.commit()
    flash ('Report successful')
    return redirect(url_for('home'), code=302)

@app.route('/report')
@login_required
def report():
    return render_template('report.html', 
                           year = datetime.now().year)

@app.route('/user/signup', methods=['POST'])
def user_signup():
    username = request.form.get('username')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User(username=username, password=password, name=name, email=email)
    if user is not None:
        db.session.add(user)
        db.session.commit()
    flash('User added successfully')
    return redirect(url_for('home'), code=302)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html',
                               year = datetime.now().year)
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user is None or user.verify_password(password) is False:
        flash('Invalid username or password')
        return render_template('login.html', 
                               year = datetime.now().year)
    flash('Login successful')
    login_user(user)
    g.user = user
    return redirect(request.args.get('next') or url_for('home'))
 
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'GET':
        return render_template('profile.html',
                               year = datetime.now().year)
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    conf_password = request.form.get('confirm_password')

    if new_password != conf_password:
        flash('New password does not match with confirm password')
        return render_template('profile.html', 
                               year = datetime.now().year)
    user = User.query.filter_by(username=g.user.username).first()
    if user is None or user.verify_password(old_password) is False:
        flash('Invalid username or password')
        return render_template('profile.html', 
                               year = datetime.now().year)
    user.set_password(new_password)
    db.session.commit()
    flash('Password change successful')
    return redirect(request.args.get('next') or url_for('home'))

@app.route('/signup')
def signup():
    return render_template('signup.html',                          
                           year = datetime.now().year)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))