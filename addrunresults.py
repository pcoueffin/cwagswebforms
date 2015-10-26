import dbaccess
from dbaccess import cwagsDBSelect, cwagsDBUpdate
import csv

info_to_add = "oct16results.csv"

syntax_for_select = "update TABLE set COLUMN = NEWVALUE where id = ID;"
#update dog set cwags ='15-1095-01' where id = 8;

csvfile = open(info_to_add, 'rb')

csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
csvdict = csv.DictReader(csvfile)
table = 'run'
setcolumn = 'result'
wherecolumn = 'round'
where2column = 'dog'
for row in csvdict:
	for key in row.keys():
		if key == setcolumn:
			column = key
			newvalue = row[key]
		elif key == wherecolumn:
			where1= key
			round = row[key]
		elif key == where2column:
			where2= key
			dog = row[key]

		else:
			id= row[key]
	if id:
		print id
		build_select_query = "update "+table+" set "+column+" = "+newvalue+" where "+where1+" = "+round+" and "+where2+" = "+dog+";"
		print build_select_query
		rowselect = cwagsDBUpdate(build_select_query,0,0,0)
	else:
		pass

changedruns ={50:[10,1], 30:[7,0], 56:[11,1]}
for entry in changedruns.keys():
    build_select_query_special = "update "+table+" set dog = "+str(changedruns[entry][0])+", result = "+str(changedruns[entry][1])+" where id = "+str(entry)+";"
    rowselect = cwagsDBUpdate(build_select_query_special,0,0,0)