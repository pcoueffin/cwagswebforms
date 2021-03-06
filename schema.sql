create table event        (id integer  PRIMARY KEY, date timestamp, datestring varchar, location varchar, name varchar, hours integer, run_cost integer);
create table entries (Timestamp varchar,  Name varchar,  Address varchar,  Phonenumber varchar,  Emailaddress varchar,  HandlerDisability varchar,  Dogsname1 varchar,  DogsCWAGSnumber1 varchar,  Breedofdog1 varchar,  DogReactivity1 varchar,  SignupforOctoberRoundsforthisdog1 varchar,  Wouldyouliketoregisteranotherdog2 varchar,  Dogsname2 varchar,  DogsCWAGSnumber2 varchar,  Breedofdog2 varchar,  DogReactivity2 varchar,  SignupforOctoberRoundsforthisdog2 varchar,  Wouldyouliketoregisteranotherdog3 varchar,  Dogsname3 varchar,  DogsCWAGSnumber3 varchar,  Breedofdog3 varchar,  DogReactivity3 varchar,  SignupforOctoberRoundsforthisdog3 varchar,  Thisquestionallowsmultipledogsperform varchar,  Pleaseaddanynoteshere varchar,  Paymentmethod varchar,  AddPaymentdetailsifapplicable varchar);
create table person       (id integer  PRIMARY KEY, name varchar, address varchar, email varchar, phone varchar, disabilities varchar);
create table dog          (id integer PRIMARY KEY, name varchar, breed varchar, cwags varchar, reactivity varchar, owner integer REFERENCES person(id));
create table judge        (id integer PRIMARY KEY REFERENCES person(id));
create table round        (id integer PRIMARY KEY, event integer REFERENCES event(id), idx integer, level integer, judge integer REFERENCES judge(id), ring integer, course char);
create table run        (id integer PRIMARY KEY autoincrement, dog integer REFERENCES dog(id), round integer REFERENCES round(id), result integer);
CREATE TABLE forms(ID INT PRIMARY KEY    NOT NULL, dataid   INT   NOT NULL, datatype  TEXT  NOT NULL, dataname   TEXT   NOT NULL, datalength INT NOT NULL, formtype text);

insert into event (datestring, location, name) values ("July 31, 2015",     "Kamloops", "CWAGS July 31");
insert into event (datestring, location, name) values ("January 25, 2015",  "Kamloops", "CWAGS Scent - Jan 25");
insert into event (datestring, location, name) values ("February 22, 2015", "Kamloops", "Feb 22 CWAGS Trial");

insert into event (date, datestring, location, hours, run_cost)
       values ("2015-10-16", "October 16, 2015", 1,2,15);
insert into event (date, datestring, location)
       values ("2015-10-23","October 23, 2015", 1);
insert into event (date, datestring, location)
       values ("2015-10-30","October 30, 2015",1);
insert into event (date, datestring, location)
       values("2015-11-06","November 6, 2015",1);
insert into event (date, datestring, location)
       values("2015-11-20","November 20, 2015",1);
insert into event (date, datestring, location)
       values("2015-11-27","November 27, 2015", 1);
insert into event (date, datestring, location)
       values("2015-12-18","December 18, 2015", 1);


CREATE VIEW maximum_runs AS SELECT event.id AS event, event.hours, count(round.id) AS number_of_rounds, 2.5 AS average_run_time, event.run_cost FROM round, event WHERE event.id = round.event GROUP BY event.id;

CREATE VIEW income AS SELECT event, number_of_rounds*10 AS course_build_time, ((hours * 60) - (number_of_rounds * 10)) as number_of_runs, (((hours * 60) - (number_of_rounds * 10)) / average_run_time) * run_cost as income from maximum_runs;

CREATE VIEW running_order AS SELECT run.dog, dog.id, dog.name, run.round, round.event, round.level FROM run LEFT JOIN dog ON run.dog = dog.id LEFT JOIN round ON run.round = round.id ORDER BY round.id;

--This is the stuff for the cork login database
CREATE TABLE users (username TEXT PRIMARY KEY ASC,role TEXT ,hash TEXT ,email_addr TEXT ,desc TEXT ,creation_date TEXT ,last_login TEXT );
CREATE TABLE roles (role TEXT PRIMARY KEY ASC,level INTEGER );
CREATE TABLE register (code TEXT PRIMARY KEY ASC,username TEXT ,role TEXT ,hash TEXT ,email_addr TEXT ,desc TEXT ,creation_date TEXT );