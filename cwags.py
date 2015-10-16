import sqlite3
from bottle import route, run, debug, template, request

def cwagsDBSelect(query, params=None, scope="all"):
    c=cwagsDB().cursor()
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

def cwagsDBUpdate(table, id, params):
    idx=0
    # THIS IS SO VERY IMMORAL.  I'm sorry little Bobby Tables! 
    query="UPDATE %s SET " % table
    for key in params:        
        if idx > 0:
            query += ", "
        query += key + ' = "' + params[key] + '"'
        idx += 1
    query += " WHERE id = " + str(id)
    print query
    c=cwagsDB()
    c.execute(query)
    c.commit()
    

def cwagsDB():
    return sqlite3.connect('cwags.sqlite')



class CWAGSDbResult:
    def __init__(self, names, values, scope):
        if (names != None):
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

@route('/person', method='GET')
@route('/person/new', method='GET')
def person():
    return template('edit_person', results=cwagsDBSelect("select NULL as name, NULL as address, NULL as phone, NULL as email", scope="one"), action="/person/-1", id=-1)

@route('/person/<id:int>', method='POST')
def personUpdate(id):
    if (id >= 0):
        print "UPDATE... person " + str(id)
        if "save" in request.forms.keys():
            del(request.forms["save"])
        # cwagsDBSelect("UPDATE person set name= :name, address= :address, phone= :phone, email= :email WHERE id = :id", {"name": request.forms.get("name"), "address": request.forms.get("address"), "phone": request.forms.get("phone"), "email": request.forms.get("email"), "id": id})
        cwagsDBUpdate("person", id, request.forms)
    else:
        print "INSERT... person"
        cwagsDBSelect("INSERT INTO person(name, address, phone, email) VALUES (:name, :address, :phone, :email)", {"name": request.forms.get("name"), "address": request.forms.get("address"), "phone": request.forms.get("phone"), "email": request.forms.get("email")})
        res = cwagsDBSelect("SELECT last_insert_rowid()", scope="one")
    return template('edit_person', results=cwagsDBSelect("SELECT name, address, phone, email FROM person WHERE id = :id", {"id": id}, scope="one"), action=("/person/" + str(id)), id=id)
    
@route('/register')
def form():
    return template('registration_page', rows=cwagsDBSelect("SELECT datatype, dataid, dataname, datalength FROM forms"))

@route('/createEntries')
def update():
    cwagsDBSelect("Insert into entries(roundid, dogid) VALUES (:roundid, :dogid)", {"roundid":} )

debug(True)
run(reloader=True)
