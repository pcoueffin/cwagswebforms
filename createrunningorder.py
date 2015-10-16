arleigh1 = "Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4"
arleigh2 = " Oct 16 Level 1 Round 1, Oct 16 Level 1 Round 3, Oct 30 Round 3 Level 1"
runs1 = arleigh1.split(',')
entries={}
for run in arleigh2.split(','):
    runs1.append(run)
#print runs1
nume= len(runs1)
#entries['arleigh'] = runs1

fiona1="Oct 16 Level 1 Round 1, Oct 16 Level 2 Round 2, Oct 23 Round 3 Level 1, Oct 23 Round 4 Level 2, Oct 30 Round 5 Level 2, Oct 30 Round 6 Level 2"
fiona=fiona1.split(',')
#entries['fiona']=fiona

selena=" Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 30 Round 2 Level 2"
ann=" Oct 16 Level 1 Round 1, Oct 16 Level 2 Round 2, Oct 30 Round 1 Level 1, Oct 30 Round 2 Level 2, Oct 30 Round 3 Level 1, Oct 30 Round 4 Level 2, Oct 30 Round 5 Level 2, Oct 30 Round 6 Level 2"
deb=" Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 23 Round 2 Level 2, Oct 23 Round 4 Level 2, Oct 30 Round 2 Level 2, Oct 30 Round 4 Level 2, Oct 16 Level 1 Round 1, Oct 16 Level 1 Round 3, Oct 23 Round 1 Level 1, Oct 23 Round 3 Level 1, Oct 30 Round 1 Level 1, Oct 30 Round 3 Level 1"
george = "Oct 16 Level 2 Round 2, Oct 16 Level 2 Round 4, Oct 23 Round 2 Level 2, Oct 23 Round 4 Level 2, Oct 30 Round 2 Level 2, Oct 30 Round 4 Level 2"
listofdata = {}
def datatodict(name, rawdata):
   # print rawdata
    #print 
    #print "-----"
    data = rawdata.split(',')
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



    
datatodict('fiona', fiona1)
datatodict('ann', ann)
datatodict('selena', selena)
datatodict('deb', deb)
datatodict('george', george)


#print entries

oct16orderR1 = []

oct16orderR2 = []
oct16order = {}

for key in entries:
    #print entries
    for uniqueid in entries[key].keys():
        entry = entries[key][uniqueid]
        print entry
        if "16" in entry[0]:
            if '1' in entry[2]:
                toRoundOneOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR1.append(toRoundOneOrder)
            if '2' in entry[2]:
                toRoundTwoOrder = [key," level ",entry[1]," round ", entry[2]]
                oct16orderR2.append(toRoundTwoOrder)
    oct16order["One"] = oct16orderR1
    oct16order["Two"] = oct16orderR2
    print oct16order

print oct16order
