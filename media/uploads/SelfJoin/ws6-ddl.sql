# WS6-1 Cinema
Create table Cinema (
seat_id int primary key auto_increment, 
free bool);
insert into Cinema (seat_id, free) values ('1', '1');
insert into Cinema (seat_id, free) values ('2', '0');
insert into Cinema (seat_id, free) values ('3', '1');
insert into Cinema (seat_id, free) values ('4', '1');
insert into Cinema (seat_id, free) values ('5', '1');
# WS6-2 Activies
Drop table Activity;
Create table Activity (
player_id int,
device_id int,
event_date date,
games_played int);
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-05-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
# WS6-3 
Drop table Grades;
Create table Grades (
student_name varchar(20), 
gender varchar(1), 
day date, 
grade int)
;
insert into Grades (student_name, gender, day, grade) values ('Aron', 'F', '2020-01-01', '17');
insert into Grades (student_name, gender, day, grade) values ('Alice', 'F', '2020-01-07', '23');
insert into Grades (student_name, gender, day, grade) values ('Bajrang', 'M', '2020-01-07', '7');
insert into Grades (student_name, gender, day, grade) values ('Khali', 'M', '2019-12-25', '11');
insert into Grades (student_name, gender, day, grade) values ('Slaman', 'M', '2019-12-30', '13');
insert into Grades (student_name, gender, day, grade) values ('Joe', 'M', '2019-12-31', '3');
insert into Grades (student_name, gender, day, grade) values ('Jose', 'M', '2019-12-18', '2');
insert into Grades (student_name, gender, day, grade) values ('Priya', 'F', '2019-12-31', '23');
insert into Grades (student_name, gender, day, grade) values ('Priyanka', 'F', '2019-12-30', '17');
