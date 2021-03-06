# My GRE Tracker

from flask import *
import sqlite3
from contextlib import closing
from sql import *
from parse import *

'''
DATABASE = 'app.db'
DEBUG = True
SECRET_KEY = 'dev key'
USERNAME = 'admin'
PASSWORD = 'admin'
'''

app = Flask(__name__)

app.secret_key = "ball is life"
app.database = "gre.db"

def connect_db():
	return sqlite3.connect(app.database)

@app.route('/')
def index():
	g.db = connect_db()
	cur = g.db.execute('select * from scores')
	scores = [dict(datetaken = row[0], test = row[1], quant = row[2], verbal = row[3]) for row in cur.fetchall()]

	cur = g.db.execute('select * from users')
	global targets
	targets = [dict(user= row[0], quanttarget = row[2], verbaltarget = row[3]) for row in cur.fetchall()]
	g.db.close()

	#myquant = 165
	#myverbal = 155

	#quantpercent = 100 * float(myquant)/float(170)
	#verbalpercent = 100 * float(myverbal)/float(170)

	return render_template("index.html", targets = targets, scores = scores)

@app.route('/addnew')
def addnew():
	#g.db.execute('insert into scores (test, datetaken, quant, verbal) values (?,?,?,?)', [request.form['test'], request.form['datetaken'], request.form['quant'], request.form['verbal']])
	return render_template("addnew.html")

@app.route('/addscore', methods = ['POST'])
def addscore():
	g.db = connect_db()
	cur = g.db.execute('insert into scores (test, datetaken, quant, verbal) values (?,?,?,?)', [request.form['test'], request.form['datetaken'], request.form['quant'], request.form['verbal']])
	g.db.commit()
	g.db.close()
	flash('Added score')
	return redirect(url_for('index'))

@app.route('/quant')
def quant():
	topics = parse("quant")
	g.db = connect_db()
	cur = g.db.execute('select * from quantpractice')
	practice = [dict(topic = row[0], date = row[1], correct = row[2], total = row[3]) for row in cur.fetchall()]
	g.db.close()

	return render_template("quant.html",topics = topics, practice = practice)

@app.route('/verbal')
def verbal():
	topics = parse("verbal")
	#g.db = connect_db()
	#cur = g.db.execute('select * from quantpractice')
	#practice = [dict(topic = row[0], date = row[1], correct = row[2], total = row[3]) for row in cur.fetchall()]
	#g.db.close()

	return render_template("verbal.html", topics = topics)
	#, practice = practice)

@app.route('/quantlog')
def quantlog():
	return render_template("newpractice.html")

@app.route('/addpractice', methods = ['POST'])
def addpractice():
	g.db = connect_db()
	cur = g.db.execute('insert into quantpractice (topic, date, correct, total) values (?,?,?,?)', [request.form['topic'], request.form['date'], request.form['correct'], request.form['total']])
	g.db.commit()
	g.db.close()
	flash('Practice Logged!')
	return redirect(url_for('quant'))

if __name__ == '__main__':
	app.run(debug = True)