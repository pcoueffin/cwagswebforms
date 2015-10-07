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
        "all": lambda: iter(c.fetchall()),
        "one": lambda: iter(c.fetchone())
    }).get(scope)()
    names=c.description
    return CWAGSDbResult(names, res, scope)


class CWAGSDbResult:
    def __init__(self, names, values, scope):
        print "dbresult: names = " + str([name[0] for name in names]) \
            + " vals = " + str(values) + " scope = " + scope
        self.names  = [name[0] for name in names]
        self.values = values
        self.idx    = 0
        self.scope  = scope

    def __iter__(self):
        return self

    def next(self):
        val=self.values.next()
        ret={}
        if (self.scope=="all"):
            ret = dict(zip(self.names, val))
        else:
            name=self.names[self.idx]
            self.idx+=1
            ret={name: val}
        print "From hell: " + str(ret)
        return ret
    
    #Python 3 compat:
    def __next__(self):
        return self.next(self)

@route('/people')
def people():
    return template('make_table', rows=cwagsDBSelect("SELECT id, name FROM person"))

@route('/person/<id:int>', method='GET')
def person(id):
    return template('edit_person', results=cwagsDBSelect("select name, address, phone, email FROM person where id = :id", {"id": id}, scope="one"), action=("/person/" + str(id)), id=id)

@route('/person/<no:int>', method='POST')
def personUpdate(no):
    print "UPDATE... person " + str(no)
    print (request.forms.get('name'))
    return template('edit_person', results=cwagsDBSelect("select name, address, phone, email FROM person where id = :id", {"id": no}, scope="one"), action=("/person/" + str(no)), id=no)
    
@route('/register')
def form():
    return template('make_form', rows=cwagsDBSelect("SELECT datatype, dataid, dataname FROM forms"), action=("/register"))



debug(True)
run(reloader=True)
