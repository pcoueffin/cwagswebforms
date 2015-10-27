import sqlite3
from bottle import route, run, debug, template, request, static_file
import bottle

#CORK STUFF HERE
#import bottle
from beaker.middleware import SessionMiddleware
from cork import Cork
import logging
bottle.TEMPLATES.clear()

logging.basicConfig(format='localhost - - [%(asctime)s] %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)
bottle.debug(True)

# Use users.json and roles.json in the local example_conf directory
#aaa = Cork('/home/cwags/cwagswebforms/example_conf', email_sender='hdsheena@gmail.com', smtp_url='startttls://hdsheena@gmail.com:mysprintmydogsmylife@smtp.gmail.com:587')

#should make it use sqlite
from cork.backends import SQLiteBackend
sb = SQLiteBackend('cwags.sqlite')
aaa = Cork(backend=sb)

# alias the authorization decorator with defaults
authorize = aaa.make_auth_decorator(fail_redirect="/login", role="user")

import datetime
app = bottle.app()
session_opts = {
    'session.cookie_expires': True,
    'session.encrypt_key': 'please use a random key and keep it secret!',
    'session.httponly': True,
    'session.timeout': 3600 * 24,  # 1 day
    'session.type': 'cookie',
    'session.validate_key': True,
}
app = SessionMiddleware(app, session_opts)


# #  Bottle methods  # #

def postd():
    return bottle.request.forms


def post_get(name, default=''):
    result = bottle.request.POST.get(name, default).strip()
    print result
    return result

@bottle.post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    print username, password
    aaa.login(username, password, success_redirect='/', fail_redirect='/login')


@bottle.route('/logout')
def logout():
    aaa.logout(success_redirect='/login')


@bottle.post('/registering')
@bottle.view('/home/cwags/cwagswebforms/views/registration_email.tpl')
def register():
    """Send out registration email"""
    returned_output = aaa.register(post_get('username'), post_get('password'), post_get('email_address'))
    return str(returned_output)
    #return {}
    #toggle return statements here to turn emailing back on someday, and take the @view out


@bottle.route('/validate_registration/:registration_code')
def validate_registration(registration_code):
    """Validate registration, create user account"""
    aaa.validate_registration(registration_code)
    return 'Thanks. <a href="/login">Go to login</a>'


@bottle.route('/')
@authorize()
def index():
    """Only authenticated users can see this"""
    #session = bottle.request.environ.get('beaker.session')
    #aaa.require(fail_redirect='/login')
    return 'Welcome! <a href="/admin">Admin page</a> <a href="/logout">Logout</a>'


@bottle.route('/admin')
@authorize(role="admin", fail_redirect='/sorry_page')
@bottle.view('admin_page')
def admin():
    """Only admin users can see this"""
    #aaa.require(role='admin', fail_redirect='/sorry_page')
    return dict(
        current_user = aaa.current_user,
        users = aaa.list_users(),
        roles = aaa.list_roles()
    )


@bottle.post('/create_user')
def create_user():
    try:
        aaa.create_user(postd().username, postd().role, postd().password)
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_user')
def delete_user():
    try:
        aaa.delete_user(post_get('username'))
        return dict(ok=True, msg='')
    except Exception, e:
        print repr(e)
        return dict(ok=False, msg=e.message)


@bottle.post('/create_role')
def create_role():
    try:
        aaa.create_role(post_get('role'), post_get('level'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.post('/delete_role')
def delete_role():
    try:
        aaa.delete_role(post_get('role'))
        return dict(ok=True, msg='')
    except Exception, e:
        return dict(ok=False, msg=e.message)


@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}


@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p>'



#CORK ENDS HERE



def cwagsDBSelect(query, params=None, scope="all"):
    db=cwagsDB()
    c=db.cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    res=({
        "all": lambda: iter(c.fetchall()),
        "one": lambda: iter(c.fetchone())
    }).get(scope)()
    names=c.description
    db.commit()
    return CWAGSDbResult(names, res, scope)

def cwagsDBUpdate(query, table, id, params):
    #enter a fourth piece of info, the number 1, for the "usual" update method. I need it to do a plain query commit, so this is how I did it.
    idx=0
    # THIS IS SO VERY IMMORAL.  I'm sorry little Bobby Tables!
    if query == 1:
        query="UPDATE %s SET " % table
        for key in params:
            if idx > 0:
                query += ", "
            query += key + ' = "' + params[key] + '"'
            idx += 1
        query += " WHERE id = " + str(id)
    else:
        query = query
    print query
    c=cwagsDB()
    c.execute(query)
    c.commit()


def cwagsDB():
    return sqlite3.connect('/home/cwags/cwagswebforms/cwags.sqlite')



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
def newperson():
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
        cwagsDBSelect("INSERT INTO person(name, address, phone, email) VALUES (:name, :address, :phone, :email);", {"name": request.forms.get("name"), "address": request.forms.get("address"), "phone": request.forms.get("phone"), "email": request.forms.get("email")})
        res = cwagsDBSelect("SELECT last_insert_rowid()", scope="one")
    return template('edit_person', results=cwagsDBSelect("SELECT name, address, phone, email FROM person WHERE id = :id;", {"id": id}, scope="one"), action=("/person/" + str(id)), id=id)

@route('/register')
@bottle.view('/home/cwags/cwagswebforms/views/registration_form')
def registration_form():
    return {}

@route('/register', method="POST")
def post_reg():
    cwagsDBSelect("Insert into person(name, address, phone, email, disabilities) VALUES (:name, :address, :phone, :email, :disabilities)", {'name': post_get("person_name"), "address":post_get("address"), "phone":post_get("phone"), "email":post_get("email"), "disabilities":post_get("disabilities")})
    owner_id = cwagsDBSelect("select id from person where name = :name", {'name': post_get("person_name")}).next()
    cwagsDBSelect("Insert into dog(name, breed, cwags, reactivity, owner) VALUES (:name, :breed, :cwags, :reactivity, :owner)", {'name': post_get('dog_name'), 'breed': post_get('breed'), 'cwags': post_get('cwags'), 'reactivity': post_get('reactivity'), 'owner': owner_id['id']})
    return template('/home/cwags/cwagswebforms/views/registration_submitted', verify=cwagsDBSelect("Select person.name as Name, person.address, person.phone, person.email, person.disabilities, dog.name as Dog, dog.breed, dog.cwags, dog.reactivity, person.id, dog.owner, dog.id as DogId from person, dog where person.id = dog.owner AND person.name = :name", {'name': post_get('person_name')}))

@route('/find_dog')
def doglookup():
    return template('views/find_dog', rows=cwagsDBSelect("SELECT name, id FROM dog;"))

@route('/dog/<id:int>', method='GET')
def dog(id):
    dogexists = cwagsDBSelect("Select id from dog;")
    idlist = []
    for row in dogexists:
        idlist.append(row['id'])
    if id in idlist:
        return template('views/edit_runs', results=[cwagsDBSelect("select dog.name, run.result, round.level, run.id, round.id, event.date from run, dog, round, event where event.id = round.event and run.round=round.id and dog.id = run.dog and dog.id = :id order by round.id;", {"id":id}),cwagsDBSelect("select round.id as id, round.event as event_id, round.level as level, round.idx as idx, event.date as date FROM round, event where event.id = round.event and date(date)>date('now')")], action=("/dog/" + str(id)), id=id)
    else:
        print "Sorry, this dog does not exist"
        return template('views/find_dog', rows=cwagsDBSelect("SELECT name, id FROM dog;"))

@route('/dog/<id:int>', method='POST')
def dogUpdate(id):
    print "UPDATE... entries for dog " + str(id)
    if "save" in request.forms.keys():
        del(request.forms["save"])
    for entered_round in request.forms.keys():
        cwagsDBSelect("Insert into run (dog, round) VALUES(:dogid, :roundid)", {"dogid":id, "roundid":request.forms.get(entered_round)})
    return template('make_table', rows = cwagsDBSelect("select dog.name, run.result, round.level, event.date from run, dog, round, event where event.id = round.event and run.round=round.id and dog.id = run.dog and dog.id = :id order by round.id;", {"id":id}))


@route('/start')
def loadindex():
    return template('index')







"""
@bottle.post('/registered')
def registration_submitted():
    #spit info back at user
    #data =
    user = cork.User()
    return user.registration(postd().person_name, postd().address, postd().email)
    #return returned_output
    #return {}
    #toggle return statements here to turn emailing back on someday, and take the @view out


"""
#this mostly works as is
#@route('/viewrunningorder/<id:int>', method='GET')
#def update(id):
    #a quick hack to get all the rounds from each day's event with one url
#    id1 = id
#    id2 = id+6
#    ids = range(id1,id2)
#    rows = []
#    for iden in ids:
#        rows.append(cwagsDBSelect("Select dog, dogname from running_order WHERE round=:id and dog = dogid;", {'id':iden}))
#    print rows
#    return template('make_table_multi', list_of_rows=rows)



@route('/viewrunningorder/<id:int>', method='GET')
def update(id):
    eventid = id
    #rows = []
    rows = cwagsDBSelect("Select round, level, name from running_order where event = :id order by round, random();", {'id':eventid})
    #print rows
    return template('make_running_orders', rows=rows)

@route('/lookupentry/<name:path>', method='GET')
def form(name):
    dogid = cwagsDBSelect("select id from dog where name = :name", {"name": name})
    id = dogid.next()['id']
    return template('make_table_of_links', rows=cwagsDBSelect("select id, round FROM run where dog = :id", {"id": id}))

@route('/editentry/<id:int>', method='GET')
def editform(id):
    return template('edit_person', results=cwagsDBSelect("select id, round FROM run where id = :id", {"id": id}), action=("/editentry/" + str(id)), id=id)

@route('/editentry/<id:int>', method='POST')
def sendeditform(id):
    print "UPDATE... run " + str(id)
    if "save" in request.forms.keys():
        del(request.forms["save"])
    cwagsDBUpdate("run", id, request.forms)


# #  Web application main  # #

def main():

    # Start the Bottle webapp
    bottle.debug(True)
    #bottle.run()
application = app
if __name__ == "__main__":
    main()