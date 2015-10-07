create table event        (id integer  PRIMARY KEY, date timestamp, location varchar, name varchar);


create table person       (id integer  PRIMARY KEY, name varchar, address varchar, email varchar, phone varchar, disabilities varchar);
create table dog          (id integer PRIMARY KEY, name varchar, breed varchar, cwags varchar, disabilities varchar, owner integer REFERENCES person(id));
create table judge        (id integer PRIMARY KEY REFERENCES person(id));
create table round        (id integer PRIMARY KEY, event integer REFERENCES event(id), idx integer, level integer);
create table roundjudging (round integer REFERENCES round(id), judge REFERENCES judge(id));
CREATE TABLE forms(
ID INT PRIMARY KEY    NOT NULL,
dataid   INT   NOT NULL,
datatype  TEXT  NOT NULL,
dataname   TEXT   NOT NULL
, formtype text);  

insert into event (date, location, name) values ("July 31, 2015",     "Kamloops", "CWAGS July 31");
insert into event (date, location, name) values ("January 25, 2015",  "Kamloops", "CWAGS Scent - Jan 25");
insert into event (date, location, name) values ("February 22, 2015", "Kamloops", "Feb 22 CWAGS Trial");
