--cork login data
   INSERT INTO users (username, email_addr, desc, role, hash, creation_date) VALUES
        (
            'admin',
            'admin@localhost.local',
            'admin test user',
            'admin',
            'cLzRnzbEwehP6ZzTREh3A4MXJyNo+TV8Hs4//EEbPbiDoo+dmNg22f2RJC282aSwgyWv/O6s3h42qrA6iHx8yfw=',
            '2012-10-28 20:50:26.286723'
        );
        INSERT INTO roles (role, level) VALUES ('special', 200);
        INSERT INTO roles (role, level) VALUES ('admin', 100);
        INSERT INTO roles (role, level) VALUES ('editor', 60);
        INSERT INTO roles (role, level) VALUES ('user', 50);


--sample data and form for sign up
insert into forms (id, dataid, datatype, dataname, datalength) values (0, 0, 'text', 'name',15);
insert into forms (id, dataid, datatype, dataname, datalength) values (1, 1, 'text', 'address', 30);
insert into forms (id, dataid, datatype, dataname, datalength) values (2, 2, 'text', 'phone number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (3, 3, 'text', 'email address', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (4, 4, 'text', 'dog name', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (5, 5, 'text', 'dog cwags number', 10);
insert into forms (id, dataid, datatype, dataname, datalength) values (6, 6, 'text', 'breed of dog', 15);
insert into forms (id, dataid, datatype, dataname, datalength) values (7, 7, 'checkbox', 'handler - disability?', 0);
insert into forms (id, dataid, datatype, dataname, datalength) values (8, 8, 'checkbox', 'dog - reactivity?', 0);



insert into person (name,address,phone,email) values ("Courtenay Watson","485 Fortune Dr Kamloops BC V2B2J5","2505787101","licketysit@gmail.com");
insert into person (name,email) values ("Dana Gallagher","3dogslater@gmail.com");
insert into person (name,address,phone,email) values ("Shauna Moore","Box 1271 Ashcroft BC V0K1A0","2503159407","nauna@telus.net");
insert into person (name) values ("PlaceHolder Judge");
insert into judge select id from person;

insert into round (event, idx, level, judge) select event.id, 1, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops" and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 2, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 3, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 4, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id, 5, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Shauna Moore";
insert into round (event, idx, level, judge) select event.id, 6, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Shauna Moore";
insert into round (event, idx, level, judge) select event.id, 7, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id, 8, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id, 9, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,10, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,11, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,12, 1, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge) select event.id,13, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,14, 2, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Courtenay Wa
tson";
insert into round (event, idx, level, judge) select event.id,15, 3, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,16, 3, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,17, 3, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";
insert into round (event, idx, level, judge) select event.id,18, 3, judge.id from event, judge, person where datestring = "February 22, 2015" and location = "Kamloops"  and judge.id=person.id and person.name = "Dana Gallagher";


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

insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a"  from event, judge, person where event.datestring = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b"  from event, judge, person where event.datestring = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.datestring = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.datestring = "October 16, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,5,1,judge.id,1,"c" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,6,1,judge.id,1,"c" from event, judge, person where event.datestring = "October 23, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,1,1,judge.id,1,"a" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,2,2,judge.id,2,"b" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,3,1,judge.id,1,"a" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,4,2,judge.id,2,"b" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "PlaceHolder Judge";
insert into round (event, idx, level, judge, ring, course) select event.id,5,2,judge.id,1,"c" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level, judge, ring, course) select event.id,6,2,judge.id,1,"c" from event, judge, person where event.datestring = "October 30, 2015" and judge.id = person.id and person.name = "Courtenay Watson";
insert into round (event, idx, level) values(7,1,2);
insert into round (event, idx, level) values(7,2,2);
insert into round (event, idx, level) values(7,3,3);
insert into round (event, idx, level) values(7,4,3);
insert into round (event, idx, level) values(7,5,2);
insert into round (event, idx, level) values(7,6,2);
insert into round (event, idx, level) values(8,1,3);
insert into round (event, idx, level) values(8,2,3);
insert into round (event, idx, level) values(8,3,2);
insert into round (event, idx, level) values(8,4,2);
insert into round (event, idx, level) values(8,5,3);
insert into round (event, idx, level) values(8,6,3);
insert into round (event, idx, level) values(9,1,3);
insert into round (event, idx, level) values(9,2,3);
insert into round (event, idx, level) values(9,3,4);
insert into round (event, idx, level) values(9,4,4);
insert into round (event, idx, level) values(9,5,3);
insert into round (event, idx, level) values(9,6,3);
insert into round (event, idx, level) values(10,1,1);
insert into round (event, idx, level) values(10,2,2);
insert into round (event, idx, level) values(10,3,3);
insert into round (event, idx, level) values(10,4,4);
insert into round (event, idx, level) values(10,5,2);
insert into round (event, idx, level) values(10,6,3);