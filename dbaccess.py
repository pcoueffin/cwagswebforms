import sqlite3
from bottle import route, run, debug, template, request, static_file
import bottle

def cwagsDBSelect(query, params=None, scope="all"):
    c=cwagsDB().cursor()
    if params:
        c.execute(query, params)
    else:
        c.execute(query)
    res=({
        "all": lambda: iter(c.fetchall()),
        "one": lambda: iter(c.fetchone())
    }).get(scope)()
    names=c.description
    return CWAGSDbResult(names, res, scope)

def cwagsDBUpdate(query, table, id, params):
    idx=0
    # THIS IS SO VERY IMMORAL.  I'm sorry little Bobby Tables! 
	#I added the if statement so I can put queries in directly or use the fancy table, id, params code here. But I think they should be separate functions.. "build a query" and "send a query"
    if query == 1:
        query="UPDATE %s SET " % table
        for key in params:        
            if idx > 0:
                query += ", "
            query += key + ' = "' + params[key] + '"'
            idx += 1
        query += " WHERE id = " + str(id)
        print query
    else:
        query=query
    c=cwagsDB()
    c.execute(query)
    c.commit()
    

def cwagsDB():
    return sqlite3.connect('cwags.sqlite')



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
