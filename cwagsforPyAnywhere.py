import sqlite3
from bottle import route, run, debug, template, request, static_file
import bottle

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


@route('/favico.ico', method='GET')
@route('/favicon.ico', method='GET')
def get_favicon():
    return static_file('favico.ico', root='./static/images/')

@route('/people')
def people():
    print "foo"
    return template('make_link_table', rows=cwagsDBSelect("SELECT id, name FROM person"), linkcols={"id": "id", "name": "id"}, base="/person/")

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

@route('/viewrunningorder/<id:int>', method='GET')
def update(id):
    rows = cwagsDBSelect("Select dog, dogname from running_order WHERE round=:id and dog = dogid;", {'id':id})
    return template('make_table', rows=rows)

@route('/lookupentry/<name:path>', method='GET')
def form(name):
    dogid = cwagsDBSelect("select id from dog where name = :name", {"name": name})
    id = dogid.next()['id']
    return template('make_table_of_links', rows=cwagsDBSelect("select id, round FROM run where dog = :id", {"id": id}))

@route('/editentry/<id:int>', method='GET')
def form(id):
    return template('edit_person', results=cwagsDBSelect("select id, round FROM run where id = :id", {"id": id}), action=("/editentry/" + str(id)), id=id)

@route('/editentry/<id:int>', method='POST')
def form(id):
    print "UPDATE... run " + str(id)
    if "save" in request.forms.keys():
        del(request.forms["save"])
    cwagsDBUpdate("run", id, request.forms)



# #  Web application main  # #

def main():

    # Start the Bottle webapp
    bottle.debug(True)
    bottle.run(app=app, quiet=False, reloader=True, host='0.0.0.0', port=80)
app = bottle.default_app()
if __name__ == "__main__":
    main()

