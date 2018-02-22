from flask import Flask, render_template, redirect, url_for, request
from database import *


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'GET':
		return render_template('login.html')
	else:
		print User.select().where((User.username == request.form['username']) & (User.password == request.form['password'])).count()
		# res = User.select().count()
		# print res
		# for r in res:
		# 	print r.username
		# return	
		if request.form['username'] != 'admin' or request.form['password'] != '123':
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html')
		else:
			return render_template('index.html')

@app.route('/registration',methods=['POST'])
def register():
	# return request.form['username']
	# db.add(User('request.form["username"]','request.form["password"]','request.form["email"]'))
	# db.commit()

	User.create(username = request.form['username'],
		password = request.form['password'],
		email = request.form['email'])
	#User.create()
	#User.create()