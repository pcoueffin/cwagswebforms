insert into forms (id, dataid, datatype, dataname, datalength) values (0, 0, 'text', 'name',15);
insert into forms (id, dataid, datatype, dataname, datalength) values (1, 1, 'text', 'address', 30);
insert into forms (id, dataid, datatype, dataname, datalength) values (2, 2, 'text', 'phone number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (3, 3, 'text', 'email address', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (4, 4, 'text', 'dog name', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (5, 5, 'text', 'dog cwags number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (6, 6, 'text', 'breed of dog', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (7, 7, 'checkbox', 'handler - disability?', 0);
insert into forms (id, dataid, datatype, dataname, datalength) values (8, 8, 'checkbox', 'dog - reactivity?', 0);



insert into person (name,address,phone,email) values ("Couson","4J5","201","lickom");
insert into person (name,email) values ("Dgher","3do.com");
insert into person (name,address,phone,email) values ("Shaore","Box 12710","2507","nalus.net");
insert into person (name) values ("PlaceHolder Judge");
insert into judge select id from person;

insert into round (event, idx, level, judge) select event.id, 1, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops" and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 2, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 3, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 4, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 5, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Shauna Moore";
insert into round (event, idx, level, judge) select event.id, 6, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Shauna Moore";
insert into round (event, idx, level, judge) select event.id, 7, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id, 8, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id, 9, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,10, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,11, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,12, 1, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,13, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,14, 2, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,15, 3, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,16, 3, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,17, 3, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,18, 3, judge.id from event, judge, person where date = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";


insert into person (name, address, phone, email) values ("Lyon", "11319 Pri 1B4",	"2147", "kljoh.ca");

insert into person (name,address, phone, email) values ("Alitzen","31B8","2505036100","aljmail.com");
insert into person (name,address, phone, email) values ("Carber","#3B7H5","2505799711","gizmoo.ca");
insert into person (name,phone, email) values ("Deatson","77121","peil.com");
insert into person (name,address, phone, email) values ("Derxon","188S9","250","dix.ca");
insert into person (name,address, phone, email) values ("Ellcholson","15 SouTece","77877","enw.ca");
insert into person (name,address, phone, email) values ("Liorath","662 6R5","25028","aa");
insert into person (name,address, phone, email) values ("Lynaneson","1131am BC V1B1B4  ","25263","klw.ca");
insert into person (name,address, phone, email) values ("Marheen","2068 5","778-262","elus.net");
insert into person (name,address, phone, email) values ("Natian","1787 C6V8","2523","nat.ca");
insert into person (name,address, phone, email) values ("vian","135H1","258","tviaw.ca");
insert into person (name,address, phone, email) values ("Trianny","361b4","2-2210","Okana.com");
insert into person (name,address, phone, email) values ("Jerley","120G-4W6","2579","janrnet.ca");
insert into person (name,address, phone, email) values ("Ptt","82B3B8","25078","cantr.net");

insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a"  from event, judge, person where event.date = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b"  from event, judge, person where event.date = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.date = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.date = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,5,1,judge.id,1,"c" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,6,1,judge.id,1,"c" from event, judge, person where event.date = "October 23, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,5,2,judge.id,1,"c" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,6,2,judge.id,1,"c" from event, judge, person where event.date = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
