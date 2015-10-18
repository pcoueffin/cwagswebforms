import csv
import sqlite3
#from bottle import route, run, debug, template, request

n=0
csvfile = open('entries1.csv', 'rb')

spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
headings = []
"""
for row in spamreader:
    if row[0] == 'Timestamp':    
        for key in row:
            headings.append(key)
#This makes a printed string to put into schema.sql
for i in headings:
    heading = i    
    for character in [" ","'",":",".","-","?"]:    
        heading=heading.replace(character,"")
    #print heading
    #print i.strip(" ")
    #print "varchar, "
    
"""
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
    
print "anything"
for row in spamreader:
    if not row[0] == 'Timestamp':  
        print "trying something"
        values = "VALUES(\""
        for i in row:
            values+=i+"\", \""
        values+="\")"
        values=values[:-5]
        #print values
        #print len(row)
        query = "INSERT INTO entries(Timestamp, Name, Address, Phonenumber, Emailaddress, HandlerDisability, Dogsname1, DogsCWAGSnumber1, Breedofdog1, DogReactivity1, SignupforOctoberRoundsforthisdog1, Wouldyouliketoregisteranotherdog2, Dogsname2, DogsCWAGSnumber2, Breedofdog2, DogReactivity2, SignupforOctoberRoundsforthisdog2, Wouldyouliketoregisteranotherdog3, Dogsname3, DogsCWAGSnumber3, Breedofdog3, DogReactivity3, SignupforOctoberRoundsforthisdog3, Thisquestionallowsmultipledogsperform, Pleaseaddanynoteshere, Paymentmethod, AddPaymentdetailsifapplicable) "+values+")"
        #print query    
        cwagsDBSelect(query)
        #print row[0]

print "all done"
testresult = cwagsDBSelect("SELECT * from entries")
print type(testresult.next)


