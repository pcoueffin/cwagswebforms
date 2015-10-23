import dbaccess
from dbaccess import cwagsDBSelect, cwagsDBUpdate
import csv

info_to_add = "cwagsnumbers.csv"

syntax_for_select = "update TABLE set COLUMN = NEWVALUE where id = ID;"
#update dog set cwags ='15-1095-01' where id = 8;

csvfile = open(info_to_add, 'rb')

csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
csvdict = csv.DictReader(csvfile)
table = 'dog'
setcolumn = 'cwags'
wherecolumn = 'id'
for row in csvdict:
	for key in row.keys():
		if key == setcolumn:
			column = key
			newvalue = row[key]
		elif key == wherecolumn:
			where= key
			id = row[key]
		else:
			print key, row[key]
	if id:
		print id
		build_select_query = "update "+table+" set "+column+" = '"+newvalue+"' where "+where+" = "+id+";"
		print build_select_query
		rowselect = cwagsDBUpdate(build_select_query,0,0,0)
	else:
		pass
	