import sqlite3


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

def cwagsDB():
    print "connecting to database..."
    return sqlite3.connect('cwags.sqlite')




entries = cwagsDBSelect("select * from entries;")

listofdata = {}
fordatabase = {}
#entries = {}

def create_run_info(signup,uniqueid):
    #entry = {}
    info = signup.split(",")
    print info
    for data in info:
        print data, uniqueid
        roundpos = data.find("Round")
        roundnumpos = roundpos + 6
        rnd = data[roundnumpos:roundnumpos+1]
        levelpos = data.find("Level")
        levelnumpos = levelpos + 6
        level = data[levelnumpos:levelnumpos+1]
        #dateround = data.split("Round", "Level")
        #print dateround
        #roundlevel = dateround[0].split("Level")
        #print roundlevel
        #rnd = dateround[1]
        #level = roundlevel[1]
        roundid = int(rnd)
        print roundid
        eventid = lookupeventid(data)
        eventnum = eventid["id"]
        print eventnum
        roundidxx = cwagsDBSelect("Select id from round where event = :eventnum and idx = :roundid;", {"roundid":roundid, "eventnum":eventnum})
        roundidx = roundidxx.next()
        #print roundidx
        try:
            tryclause = cwagsDBSelect("Select id from run where round = :round and dog = :dog;", {"round":roundid, "dog": uniqueid})
            print tryclause.next()
            print "Try succeeded"
        except:
            print "Create this entry!", uniqueid, data
            tryclause = cwagsDBSelect("Insert into run(round, dog, result) values(:round, :dog, '');", {"round": roundidx["id"], "dog": uniqueid})
            tryclause = cwagsDBSelect("Select id from run where round = :round and dog = :dog;", {"round":roundid, "dog": uniqueid})

def lookupeventid(datafrominfo):
    datedictionary = {16: "October 16, 2015", 23: "October 23, 2015", 30: "October 30, 2015", 6: "November 06, 2015", 20: "November 20, 2015", 27: "November 27, 2015", 18: "December 18, 2015"}
    #datafrominfo = "Oct 23 Round 4 Level 2"
    datenumbers = datafrominfo.strip()
    print datenumbers
    relevantdata = int(datenumbers[4:6])
    try:
        date = datedictionary[relevantdata]
        print date
    except:
        print relevantdata, datafrominfo
    try:
        eventid = cwagsDBSelect("Select id from event where datestring like :date", {"date": date})
        return eventid.next()
    except:
        print "This date didn't input correctly"

def lookupdog(dogentrystring,num):
    num = str(num)
    name = dogentrystring['Dogsname'+num]
    print "Looking up dog " + name
    person = dogentrystring['Name']
    breed=dogentrystring['Breedofdog'+num]
    cwags = dogentrystring['DogsCWAGSnumber'+num]
    reactivity = dogentrystring['DogReactivity'+num]
    owner = lookupowner(person, dogentrystring)
    #print type(owner)
    #print owner.names
    uniqueid = cwagsDBSelect("Select id from dog where name like :name;", {"name": name})
    try:
        return uniqueid.next()
    except:
        print name
        cwagsDBSelect("insert into dog(name, breed, cwags, reactivity, owner) values(:name, :breed, :cwags, :reactivity, :owner);", {"name":name, "breed":breed, "cwags":cwags, "reactivity":reactivity, "owner":owner["id"]})
        print "Create this record"
        uniqueid=cwagsDBSelect("Select id from dog where name like :name;", {"name": name})
        return uniqueid.next()

def lookupowner(fromlookupdog, dog):
    name = fromlookupdog
    email = dog["Emailaddress"]
    address = dog["Address"]
    phone = dog["Phonenumber"]
    disabilities = dog["HandlerDisability"]
    uniqueid = cwagsDBSelect("select id from person where name like :name;", {"name": fromlookupdog})
    try:
        return uniqueid.next()
    except:
        cwagsDBSelect("insert into person(name, address, email, phone, disabilities) values(:name, :address, :email, :phone, :disabilities);", {"name":name, "address":address, "email":email, "phone":phone, "disabilities":disabilities})
        uniqueid = cwagsDBSelect("select id from person where name like :name;", {"name": name})
        return uniqueid.next()


for entry in entries:
    #print "test"
    uniqueid1 = lookupdog(entry,1)
    print 'unique', uniqueid1
    print "creating an entry"
    try:
        create_run_info(entry['SignupforOctoberRoundsforthisdog1'],uniqueid1['id'])
    except:
        print "this dog has no entries?"
        pass
    #check for second dog
    if len(entry['Dogsname2'])>1 :
        uniqueid2 = lookupdog(entry,2)
        create_run_info(entry['SignupforOctoberRoundsforthisdog2'],uniqueid2['id'])

