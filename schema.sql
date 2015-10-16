create table event        (id integer  PRIMARY KEY, date timestamp, location varchar, name varchar, hours integer, run_cost integer);
create table entries (Timestamp varchar,  Name varchar,  Address varchar,  Phonenumber varchar,  Emailaddress varchar,  HandlerDisability varchar,  Dogsname1 varchar,  DogsCWAGSnumber1 varchar,  Breedofdog1 varchar,  DogReactivity1 varchar,  SignupforOctoberRoundsforthisdog1 varchar,  Wouldyouliketoregisteranotherdog2 varchar,  Dogsname2 varchar,  DogsCWAGSnumber2 varchar,  Breedofdog2 varchar,  DogReactivity2 varchar,  SignupforOctoberRoundsforthisdog2 varchar,  Wouldyouliketoregisteranotherdog3 varchar,  Dogsname3 varchar,  DogsCWAGSnumber3 varchar,  Breedofdog3 varchar,  DogReactivity3 varchar,  SignupforOctoberRoundsforthisdog3 varchar,  Thisquestionallowsmultipledogsperform varchar,  Pleaseaddanynoteshere varchar,  Paymentmethod varchar,  AddPaymentdetailsifapplicable varchar);
create table person       (id integer  PRIMARY KEY, name varchar, address varchar, email varchar, phone varchar, disabilities varchar);
create table dog          (id integer PRIMARY KEY, name varchar, breed varchar, cwags varchar, disabilities varchar, owner integer REFERENCES person(id));
create table judge        (id integer PRIMARY KEY REFERENCES person(id));
create table round        (id integer PRIMARY KEY, event integer REFERENCES event(id), idx integer, level integer, judge integer REFERENCES judge(id), ring integer, course char);

CREATE TABLE forms(ID INT PRIMARY KEY    NOT NULL, dataid   INT   NOT NULL, datatype  TEXT  NOT NULL, dataname   TEXT   NOT NULL, datalength INT NOT NULL, formtype text);  

insert into event (date, location, name) values ("July 31, 2015",     "Kamloops", "CWAGS July 31");
insert into event (date, location, name) values ("January 25, 2015",  "Kamloops", "CWAGS Scent - Jan 25");
insert into event (date, location, name) values ("February 22, 2015", "Kamloops", "Feb 22 CWAGS Trial");

insert into event (date, location, hours, run_cost) 
       values ("October 16, 2015",1,2,15);
insert into event (date, location) 
       values ("October 23, 2015",1);
insert into event (date, location) 
       values ("October 30, 2015",1);
insert into event (date, location) 
       values("November 06, 2015",1);
insert into event (date, location) 
       values("November 20, 2015",1);
insert into event (date, location) 
       values("November 27, 2015",1);
insert into event (date, location) 
       values("December 18, 2015",1);


CREATE VIEW maximum_runs AS SELECT event.id AS event, event.hours, count(round.id) AS number_of_rounds, 2.5 AS average_run_time, event.run_cost FROM round, event WHERE event.id = round.event GROUP BY event.id;

CREATE VIEW income AS SELECT event, number_of_rounds*10 AS course_build_time, ((hours * 60) - (number_of_rounds * 10)) as number_of_runs, (((hours * 60) - (number_of_rounds * 10)) / average_run_time) * run_cost as income from maximum_runs;

