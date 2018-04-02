import pandas as pd
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import Flask, session, render_template, request, redirect, g, url_for
from database import *
import os

app =Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        users = User.select().where((User.username == request.form['username']) & ((User.password == request.form['password'])))
        if users:
            session['user'] = request.form['username']
            return redirect(url_for('protected'))

    return render_template('login.html')

@app.route('/home')
def protected():
    if g.user:
        return render_template('index.html',user = session['user'])

    return redirect(url_for('index'))

@app.route('/add')
def add():
    if g.user:
        return render_template('plain_page.html',user = session['user'])

    return redirect(url_for('protected'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'You are not Logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/registration',methods=['POST'])
def register():
	status = User.create(username = request.form['username'],
		password = request.form['password'],
		email = request.form['email'])
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
