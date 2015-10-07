import sqlite3
from bottle import route, run, debug, template, request

def cwagsDBSelect(query, params=None, scope="all"):
    conn=sqlite3.connect('cwags.sqlite')
    c=conn.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    res=({
        "all": lambda: c.fetchall(),
        "one": lambda: c.fetchone()
    }).get(scope)()
    names=c.description
    return (names, res)

'''
def assigntovariables(selects, froms):
	rowdict = {}
	for column in selects:
		columnid = column
		sqlStatement = "SELECT " + column + " FROM " + froms
		rowdict[columnid] = cwagsDBSelect(sqlStatement)
	return rowdict
'''

@route('/people')
def people():
    return template('make_table', rows=cwagsDBSelect("SELECT id, name FROM person")[1])

@route('/person/<no:int>', method='GET')
def person(no):
    return template('edit_person', results=cwagsDBSelect("select name, address, phone, email FROM person where id = :id", {"id": no}, scope="one"), action=("/person/" + str(no)), id=no)

@route('/person/<no:int>', method='POST')
def personUpdate(no):
    print "UPDATE... person " + str(no)
    print (request.forms.get('name'))
    return template('edit_person', results=cwagsDBSelect("select name, address, phone, email FROM person where id = :id", {"id": no}, scope="one"), action=("/person/" + str(no)), id=no)
    
@route('/register', method='GET')
def form():
	return template('make_form', results=cwagsDBSelect("SELECT datatype, dataid, dataname FROM forms"), action=("/register"))

@route('/register', method="POST")
def formSend():
	print request.forms.keys(), request.forms.values()
	

debug(True)
run(reloader=True)
