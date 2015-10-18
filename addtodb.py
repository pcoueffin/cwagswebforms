import csv
n=0
csvfile = open('entries.csv', 'rb')
csvfile1 = csvfile

spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

for row in spamreader:
    print row[4]

entry = 1
#readfile = csv.DictReader(csvfile, delimiter=',', quotechar='"')
#dialect = csv.Sniffer().sniff(csvfile.read())
#csvfile.seek(0)
readfile = csv.reader(csvfile1, delimiter=',')
for row in readfile:
    for r in row:
        print r
#print reader[1]
dictofentries = {}
entries= {}
#dictofentries = dict.fromkeys(reader[1],0)

for somerow in readfile:
    n += 1
    stupidcsv = somerow
    #print "____"
    #print row
    #print n
    
    dictofentries[n]=stupidcsv
#keys = dictofentries[1]

def create_dict_of_user_submission(submissionrow):
    for key in keys:
        number = keys.index(key)
        dictname =  dictofentries[submissionrow][0]
#        dictname[key] = dictofentries[submissionrow][number]
"""       
for number in range(2,len(dictofentries.keys())):
    dictname = number
    create_dict_of_user_submission(n)
"""
x = {}
print spamreader
print ")____________"

for row in spamreader:
    print row
    rowkey = row[1]
    print rowkey
    x[rowkey] = {} # derive this from something.
    for idx, col in enumerate(row):
        print idx
        x[rowkey][idx] = col
print x
            #print submittedinfo
            
         #   value = submittedinfo
        #entries[key]=value
        
print entries
    #for i in dictofentries:
     #   entries[]
"""        
        for i in row.keys():
            print i, ": ",  row[i]
            i = row[i]
        name = row['Name']
        address = row['Address']
        print name, "++++", address
#        print "pkiuhio"
    
        
"""