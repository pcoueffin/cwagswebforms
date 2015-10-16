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
    print "connecting..."
    return sqlite3.connect('cwags.sqlite')
    
    



Trbel="Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 30 Round 4 Level 2"
Barbie="Oct 16 Level 1 Round 1, Oct 16 Level 2 Round 2, Oct 23 Round 3 Level 1, Oct 23 Round 4 Level 2, Oct 30 Round 5 Level 2, Oct 30 Round 6 Level 2"
Spring="Oct 16 Level 1 Round 1, Oct 16 Level 2 Round 2, Oct 30 Round 1 Level 1, Oct 30 Round 2 Level 2, Oct 30 Round 3 Level 1, Oct 30 Round 4 Level 2, Oct 30 Round 5 Level 2, Oct 30 Round 6 Level 2"
Joy="Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 30 Round 2 Level 2"
Hunter="Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 23 Round 2 Level 2, Oct 23 Round 4 Level 2, Oct 30 Round 2 Level 2, Oct 30 Round 4 Level 2"
Chloe="Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 23 Round 2 Level 2, Oct 23 Round 4 Level 2, Oct 30 Round 2 Level 2, Oct 30 Round 4 Level 2"
Joey="Oct 16 Level 1 Round 1, Oct 16 Level 2 Round 2"
Jazz="Oct 16 Level 1 Round 1, Oct 16 Level 1 Round 3, Oct 30 Round 3 Level 1"
China="Oct 16 Level 1 Round 1, Oct 16 Level 1 Round 3, Oct 23 Round 1 Level 1, Oct 23 Round 3 Level 1, Oct 30 Round 1 Level 1, Oct 30 Round 3 Level 1"
Indigo="Oct 16 Level 1 Round 3, Oct 16 Level 2 Round 4"

dogs = cwagsDBSelect("select SignupforOctoberRoundsforthisdog1 from entries;")
print dogs

listofdata = {}
fordatabase = {}
entries = {}
def datatodict(name, rawdata):
   # print rawdata
    #print 
    #print "-----"
    data = rawdata.split(',')
    fordatabase[name]=data
    for i in data:
        uniqueid= data.index(i)
        listofdata[uniqueid]=i
        #listofdata.append(uniqueid)
        #data.append(str(data.index(i)))
    #print name, data
    #print listofdata
    entry = {}
    for uniqueid in listofdata.keys():
        #uniqueid = uniqueid
        data=listofdata[uniqueid]
        if "16" in listofdata[uniqueid]:
            dateround = data.split("Round")
            roundlevel = dateround[0].split("Level")
            date = roundlevel[0]
            #print roundlevel
            rnd = dateround[1]
            level = roundlevel[1]
            
        else:
            dateround = data.split("Round")
            roundlevel = dateround[1].split("Level")
            date =  dateround[0]
            rnd = roundlevel[0]
            level = roundlevel[1]
            #print level, date, rnd
        entry[uniqueid] = [date, level, rnd]
    entries[name]= entry





    
datatodict('Trbel', Trbel)
datatodict('Barbie', Barbie)
datatodict('China', China)
datatodict('Chloe', Chloe)
datatodict('Hunter', Hunter)

datatodict('Indigo', Indigo)

datatodict('Jazz', Jazz)

datatodict('Joey', Joey)

datatodict('Joy', Joy)

datatodict('Spring', Spring)

#print entries

oct16orderR1 = []

oct16orderR2 = []
oct16orderR3 = []
oct16orderR4 = []
oct16order = {}

for key in entries:
    #print entries
    for uniqueid in entries[key].keys():
        entry = entries[key][uniqueid]
        #print entry
        if "16" in entry[0]:
            if '1' in entry[2]:
                toRoundOneOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR1.append(toRoundOneOrder)
            if '2' in entry[2]:
                toRoundTwoOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR2.append(toRoundTwoOrder)
            if '3' in entry[2]:
                toRoundThreeOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR3.append(toRoundThreeOrder)
            if '4' in entry[2]:
                toRoundFourOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR4.append(toRoundFourOrder)
    oct16order["One"] = oct16orderR1
    oct16order["Two"] = oct16orderR2
    oct16order["Three"] = oct16orderR3
    oct16order["Four"] = oct16orderR4
    #print oct16order

for key in ["One", "Two", "Three", "Four"]:
    print "Round " + key
    for entry in oct16order[key]:
        print entry[0]
    print "_____________________"
    
