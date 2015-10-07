insert into forms (id, dataid, datatype, dataname, datalength) values (1, 1, 'text', '
phone number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (2, 2, 'text', 'name',15);
insert into forms (id, dataid, datatype, dataname, datalength) values (3, 3, 'checkbox', '
handler - disability?', 0);
insert into forms (id, dataid, datatype, dataname, datalength) values (4, 4, 'text', '
address', 30);
insert into forms (id, dataid, datatype, dataname, datalength) values (5, 5, 'checkbox', '
dog - reactivity?
', 0);
insert into forms (id, dataid, datatype, dataname, datalength) values (6, 6, 'text', '
email address', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (7, 7, 'text', '
breed of dog', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (8, 8, 'text', '
dog cwags number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (9, 9, 'text', '
dog name', 10);





insert into person (name,address,phone,email) values ("Courtenay Watson","485 Fortune Dr Kamloops BC V2B2J5","2505787101","licketysit@gmail.com");
insert into person (name,email) values ("Dana Gallagher","3dogslater@gmail.com");
insert into person (name,address,phone,email) values ("Shauna Moore","Box 1271 Ashcroft BC V0K1A0","2503159407","nauna@telus.net");
insert into judge select id from person;

insert into round (event, idx, level) select id, 1, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 2, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 3, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 4, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 5, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 6, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 7, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 8, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id, 9, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,10, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,11, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,12, 1 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,13, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,14, 2 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,15, 3 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,16, 3 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,17, 3 from event where date = "February 22, 2015" and location = "Kamloops";
insert into round (event, idx, level) select id,18, 3 from event where date = "February 22, 2015" and location = "Kamloops";

select round.id, judge.id from event, round, judge, person where event.date = "February 22, 2015" and event.location = "Kamloops" and event.id = round.event and round.idx = 1 and judge.id = person.id and person.name = "Courtenay Watson";


insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 1 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 2 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 3 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 4 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 5 and judge.id = person.id 
          and person.name = "Shauna Moore";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 6 and judge.id = person.id 
          and person.name = "Shauna Moore";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 7 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 8 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 9 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 10 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 11 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 12 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 13 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 14 and judge.id = person.id 
          and person.name = "Courtenay Watson";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 15 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 16 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 17 and judge.id = person.id 
          and person.name = "Dana Gallagher";
insert into roundjudging 
    select round.id, judge.id from event, round, judge, person 
        where event.date = "February 22, 2015" and event.location = "Kamloops" 
          and event.id = round.event
          and round.idx = 18 and judge.id = person.id 
          and person.name = "Dana Gallagher";

insert into person (name, address, phone, email) values ("Lynne Johaneson", "11319 Priest Valley Drive Coldstream, BC V1B 1B4",	"2505453147", "kljohanes@shaw.ca");

insert into person (name,address, phone, email) values ("Alice Jantzen","3460 Hope Drive Armstrong B.C. V0E 1B8","2505036100","aljantzen@hotmail.com");
insert into person (name,address, phone, email) values ("Cathy Barber","#35 3665 Westsyde Road Kamloops BC V2B7H5","2505799711","gizmogeorgie@yahoo.ca");
insert into person (name,phone, email) values ("Deb Watson","7782207121","petrescuerz@gmail.com");
insert into person (name,address, phone, email) values ("Derek Dixon","1880 Red Tail Crescent Kamloops BC V2B8S9","2505541880","dixonld@shaw.ca");
insert into person (name,address, phone, email) values ("Ellen Nicholson","1558 Southview Terrace","7784704877","enichol1@shaw.ca");
insert into person (name,address, phone, email) values ("Lissa Porath","662 Sycamore Drive Kamloops BC  V2B 6R5","250-579-5228","aarcat@shaw.ca");
insert into person (name,address, phone, email) values ("Lynne Johaneson","11319 Priest Valley Drive Coldstream BC V1B1B4  ","250-351-5263","kljohanes@shaw.ca");
insert into person (name,address, phone, email) values ("Martha Goheen","2068 Monteith Drive Kamloops BC V2E 2G5","778-220-3262","cruisero@telus.net");
insert into person (name,address, phone, email) values ("Natalie Vivian","1787 Gardiner Rd Kamloops BC V2C6V8","250-573-3123","natalie-vivian@shaw.ca");
insert into person (name,address, phone, email) values ("Tanya Vivian","1357 Crestwood Drive Kamloops BC V2C 5H1","250-319-8428","tvivian@shaw.ca");
insert into person (name,address, phone, email) values ("Trishanna Ramsey","3695 coldicott dr armstrong bc v0e1b4","250-938-2210","Okanagangeckos@hotmail.com");
insert into person (name,address, phone, email) values ("Jan Wherley","1206 Chimney Valley Rd Williams Lake BC V2G-4W6","250 392-3479","janpeter@xplornet.ca");
insert into person (name,address, phone, email) values ("Pat Truitt","8227 Buchanan Rd. Coldstream B.C. V1B3B8","2502603078","cantree@telus.net");

