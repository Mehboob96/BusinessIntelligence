import pandas as pd
from flask_pymongo import PyMongo
from pymongo import MongoClient
import pprint
from flask import Flask, session, render_template, request, redirect, g, url_for,jsonify,flash
from database import *
import os
import bson
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
            flash('You were successfully logged in')
            return redirect(url_for('protected'))

    return render_template('login.html')

@app.route('/home')
def protected():
    if getsession():
        # db.balancesheet.find({"business_id":session['user']},{"assets.total":1})
         # db.balancesheet.find({"business_id":"Mehboob"}).forEach(bsonfunction(d){print(d.assets.total)})
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
        result5 = request.form.getlist('operatingtype')
        result6 = request.form.getlist('operatingamount')
        result7 = request.form.getlist('investingtype')
        result8 = request.form.getlist('investingamount')
        result9 = request.form.getlist('financingtype')
        result10 = request.form.getlist('financingamount')
        result11 = request.form.getlist('revenuetype')
        result12 = request.form.getlist('revenueamount')
        result13 = request.form.getlist('expensestype')
        result14 = request.form.getlist('expensesamount')
        totalasset = 0
        totalliability = 0
        totaloperating = 0
        totalinvesting = 0
        totalfinancing = 0
        totalrevenue = 0
        totalexpenses = 0

        assets = {}
        for i in range(len(result)-1):
            assets[result[i]] = result2[i]
            totalasset = totalasset + int(result2[i])
        assets['Total'] = totalasset

        liabilities = {}
        for i in range(len(result3)-1):
            liabilities[result3[i]] = result4[i]
            totalliability = totalliability + int(result4[i])
        liabilities['Total'] = totalliability

        operating = {}
        for i in range(len(result5)-1):
            operating[result5[i]] = result6[i]
            totaloperating = totaloperating + int(result6[i])
        operating['Total'] = totaloperating

        investing = {}
        for i in range(len(result7)-1):
            investing[result7[i]] = result8[i]
            totalinvesting = totalinvesting + int(result8[i])
        investing['Total'] = totalinvesting

        financing = {}
        for i in range(len(result9)-1):
            financing[result9[i]] = result10[i]
            totalfinancing = totalfinancing + int(result10[i])
        financing['Total'] = totalfinancing

        revenue = {}
        for i in range(len(result11)-1):
            revenue[result11[i]] = result12[i]
            totalrevenue = totalrevenue + int(result12[i])
        revenue['Total'] = totalrevenue

        expenses = {}
        for i in range(len(result13)-1):
            expenses[result13[i]] = result14[i]
            totalexpenses = totalexpenses + int(result14[i])
        expenses['Total'] = totalexpenses

        #balancesheet
        doc = {
            "business_id" : session['user'],
            "year" : int(request.form.get('year',None)),
            "month" : int(request.form.get('month',None)),
            "assets":assets,
            "liabilities":liabilities
        }

        #Cashflow
        doc2 = {
            "business_id" : session['user'],
            "year" : int(request.form.get('year',None)),
            "month" : int(request.form.get('month',None)),
            "operating":operating,
            "investing":investing,
            "financing":financing
        }

        #IncomeStatement
        doc3 = {
            "business_id" : session['user'],
            "year" : int(request.form.get('year',None)),
            "month" : int(request.form.get('month',None)),
            "revenue":revenue,
            "expenses":expenses,
        }
        # return jsonify(doc);

        db.balanceSheet.insert(doc)
        db.cashFlowStatement.insert(doc2)
        db.incomeStatement.insert(doc3)
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

@app.route('/getStatement',methods=['POST'])
def getStatement():
    s = db.balanceSheet.find({'$and':[{'business_id':session['user']},{'year':request.form['year']}]})
    s1 = db.cashFlowStatement.find({'$and':[{'business_id':session['user']},{'year':request.form['year']}]})
    # res = dumps(s,s1)
    # data = {'bs':s,'cf':s1};
    return dumps(s)

@app.route('/getBalanceSheet',methods=['POST'])
def getBalanceSheet():
    bs = db.balanceSheet.find({
        '$and':[
            {'business_id':session['user']},
            {'year':request.form['year']}
        ]
    })

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
