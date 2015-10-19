run: cwags.sqlite
	python cwags.py

cwags.sqlite: schema.sql data.sql addtodb1.py entries1.csv createentriesfromdb.py
	rm -f $@
	cat schema.sql data.sql | sqlite3 $@
	python addtodb1.py $@ entries1.csv
	python createentriesfromdb.py $@

commit:
	git commit
	git push

