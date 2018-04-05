import pandas as pd
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pprint
from flask import Flask, session, render_template, request, redirect, g, url_for,jsonify
from database import *
import os
from bson.json_util import dumps

client = MongoClient('mongodb://localhost:27017/')
db = client.example

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
    if getsession():
        db.balancesheet.find({"business_id":session['user']},{"assets.total":1})
        return render_template('index.html',user = session['user'])

    return redirect(url_for('index'))

#add new statements GUI
@app.route('/add')
def add():
    if getsession():
        return render_template('plain_page.html',user = session['user'])

    return redirect(url_for('protected'))

#add new statements in DB
@app.route('/addStatement',methods=['POST'])
def addStatement():
    if getsession():
        result = request.form.getlist('assettype')
        result2 = request.form.getlist('assetamount')
        result3 = request.form.getlist('liabilitytype')
        result4 = request.form.getlist('liabilityamount')
        totalasset = 0
        totalliability = 0

        assets = {}
        for i in range(len(result)-1):
            assets[result[i]] = result2[i]
            totalasset = totalasset + int(result2[i])

        liabilities = {}
        for i in range(len(result3)-1):
            liabilities[result3[i]] = result4[i]
            totalliability = totalliability + int(result4[i])

        doc = {
            "business_id" : session['user'],
            "year" : request.form.get('year',None),
            "month" : request.form.get('month',None),
            "assets":assets,
            "totalasset" : totalasset,
            "liabilities":liabilities,
            "totalliability": totalliability
        }
        # return jsonify(doc);

        db.balancesheet.insert(doc)
        # print "ASSETS"
        # for i in range(len(result)-1):
        #     print result[i]," : ",result2[i]
        #     totalasset = totalasset + int(result2[i])
        # print totalasset
        # print "LIABILITY"
        # for i in range(len(result3)-1):
        #     print result3[i]," : ",result4[i]
        #     totalliability = totalliability + int(result4[i])
        # print totalliability
        # f = request.form
        # for key in f.keys():
            # for value in f.getlist(key):
                # print key,":",value
        return "Success"
        # pprint.pprint(getsession())

    return redirect(url_for('index'))


@app.route('/getBalanceSheet',methods=['POST'])
def getBalanceSheet():
    bs = db.balancesheet.find({'business_id':'Mehboob'})
    return dumps(bs)

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return True

    return False

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
