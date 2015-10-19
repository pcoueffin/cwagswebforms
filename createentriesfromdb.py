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
        if "16" in data:
            dateround = data.split("Round")
            roundlevel = dateround[0].split("Level")
            date = roundlevel[0]
            #print roundlevel
            rnd = dateround[1]
            level = roundlevel[1]
            roundid = int(rnd)
            #print roundid
            roundidxx = cwagsDBSelect("Select id from round where event = 4 and idx = :roundid;", {"roundid":roundid})
            roundidx = roundidxx.next()
            #print roundidx
            try:
                tryclause = cwagsDBSelect("Select id from run where round = :round and dog = :dog;", {"round":roundid, "dog": uniqueid})
                print tryclause               
                print "Try succeeded"
            except:
                print "Create this entry!", uniqueid, data                
                tryclause = cwagsDBSelect("Insert into run(round, dog, result) values(:round, :dog, '');", {"round": roundidx["id"], "dog": uniqueid})
                tryclause = cwagsDBSelect("Select id from run where round = :round and dog = :dog;", {"round":roundid, "dog": uniqueid})
                
        else:
            #print data
            dateround = data.split("Round")
            roundlevel = dateround[1].split("Level")
            date =  dateround[0]
            rnd = roundlevel[0]
            level = roundlevel[1]
            #print level, date, rnd



def lookupdog(dogentrystring,num):
    num = str(num)
    name = dogentrystring['Dogsname'+num]
    print "Looking up dog " + name
    person = dogentrystring['Name']
    breed=dogentrystring['Breedofdog'+num]
    cwags = dogentrystring['DogsCWAGSnumber'+num]
    disabilities = dogentrystring['DogReactivity'+num]
    owner = lookupowner(person, dogentrystring)
    #print type(owner)
    #print owner.names
    uniqueid = cwagsDBSelect("Select id from dog where name like :name;", {"name": name})
    try:
        return uniqueid.next()
    except:
        print name
        cwagsDBSelect("insert into dog(name, breed, cwags, disabilities, owner) values(:name, :breed, :cwags, :disabilities, :owner);", {"name":name, "breed":breed, "cwags":cwags, "disabilities":disabilities, "owner":owner["id"]})
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
    create_run_info(entry['SignupforOctoberRoundsforthisdog1'],uniqueid1['id'])
    #check for second dog
    if len(entry['Dogsname2'])>1 :
        uniqueid2 = lookupdog(entry,2)
        create_run_info(entry['SignupforOctoberRoundsforthisdog2'],uniqueid2['id'])
    
  