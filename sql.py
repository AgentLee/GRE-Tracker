import sqlite3
import json

#with sqlite3.connect("gre.db") as connection:
#	c = connection.cursor()
#	c.execute("""CREATE TABLE scores(datetaken TEXT, test TEXT, quant INT, verbal INT)""")
#	c.execute('INSERT INTO scores VALUES("6/2015", "Diagnostic", 150, 150)')
#	c.execute('INSERT INTO scores VALUES("6/2015", "Diagnostic", 154, 144)')
#	c.execute('INSERT INTO scores VALUES("7/2015", "Diagnostic", 162, 0)')
#	c.execute('INSERT INTO scores VALUES("7/19/2015", "Diagnostic", 161, 148)')
#	c.execute('INSERT INTO scores VALUES("8/7/2015", "Diagnostic", 157, 0)')

def dbadd():
	with sqlite3.connect("gre.db") as connection:
		c = connection.cursor()
		c.execute('INSERT INTO quantpractice VALUES("barrons pt 2", "8/7/15", 27, 40)')

def addtodb(test, datetaken, quant, verbal):
	print test, datetaken, quant, verbal
	
	with sqlite3.connect("gre.db") as connection:
		c = connection.cursor()
		c.execute('INSERT INTO scores VALUES(%s, %s, %d, %d)', test, datetaken, quant, verbal)

def addtopics():
	with open("quant.json") as datafile:
		data = json.load(datafile)

	topics = []
	for i in range(len(data)):	
		topics.append([])
		for j in range(2):
			if j == 0:
				topics[i].append(str(data[i]['topic']))
			elif j == 1:
				topics[i].append(int(data[i]['videos']))

	with sqlite3.connect("gre.db") as connection:
		c = connection.cursor()

		for x in topics:
			topic = x[0]
			num = x[1]
			c.execute('INSERT INTO quanttopics VALUES(%s, %d)', topic, num)


def main():
	dbadd()

if __name__ == "__main__":
	main()

'''
with sqlite3.connect("test.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
	c.execute('INSERT INTO posts VALUES("GOOD", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
'''