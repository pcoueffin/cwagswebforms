run: cwags.sqlite
	python cwags.py

cwags.sqlite: schema.sql data.sql
	rm -f $@
	cat $^ | sqlite3 $@

commit:
	git commit
	git push

