from flask import Flask, render_template, redirect, url_for, request
from database import *

app = Flask(__name__)

@app.route('/protected')
def home():
	return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
	error = None
	if request.method == 'GET':
		return render_template('login.html')
	else:
		# print User.select().where((User.username == request.form['username']) & (User.password == request.form['password'])).count()
		# session.pop('user', None)

		if request.form['username'] == 'admin' and request.form['password'] == '123':
			# error = 'Invalid Credentials. Please try
			# session['user'] = request.form['username']
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/registration',methods=['POST'])
def register():
	User.create(username = request.form['username'],
		password = request.form['password'],
		email = request.form['email'])

if __name__ == "__main__":
	# app.debug = True
	app.run(debug=True)
