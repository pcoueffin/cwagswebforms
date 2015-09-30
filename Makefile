cwags.sqlite: schema.sql data.sql
	rm -f $@
	cat $^ | sqlite3 $@


