# WS9-1 for Project and Employee
Drop table Employee;
Create table Employee (
employee_id int, 
team_id int);
insert into Employee (employee_id, team_id) values ('1', '8');
insert into Employee (employee_id, team_id) values ('2', '8');
insert into Employee (employee_id, team_id) values ('3', '8');
insert into Employee (employee_id, team_id) values ('4', '7');
insert into Employee (employee_id, team_id) values ('5', '9');
insert into Employee (employee_id, team_id) values ('6', '9');
# WS9-2 for 
Drop table Scores;
Create table Scores (
player_name varchar(20), 
gender varchar(1), 
day date, 
score_points int)
;
insert into Scores (player_name, gender, day, score_points) values ('Aron', 'F', '2020-01-01', '17');
insert into Scores (player_name, gender, day, score_points) values ('Alice', 'F', '2020-01-07', '23');
insert into Scores (player_name, gender, day, score_points) values ('Bajrang', 'M', '2020-01-07', '7');
insert into Scores (player_name, gender, day, score_points) values ('Khali', 'M', '2019-12-25', '11');
insert into Scores (player_name, gender, day, score_points) values ('Slaman', 'M', '2019-12-30', '13');
insert into Scores (player_name, gender, day, score_points) values ('Joe', 'M', '2019-12-31', '3');
insert into Scores (player_name, gender, day, score_points) values ('Jose', 'M', '2019-12-18', '2');
insert into Scores (player_name, gender, day, score_points) values ('Priya', 'F', '2019-12-31', '23');
insert into Scores (player_name, gender, day, score_points) values ('Priyanka', 'F', '2019-12-30', '17');
# WS3 : Sales
Drop table Sales;
Create table Sales (employee_id int, product_id int, sales int);
insert into Sales (employee_id, product_id, sales) values ('2', '2', '95');
insert into Sales (employee_id, product_id, sales) values ('2', '3', '95');
insert into Sales (employee_id, product_id, sales) values ('1', '1', '90');
insert into Sales (employee_id, product_id, sales) values ('1', '2', '99');
insert into Sales (employee_id, product_id, sales) values ('3', '1', '80');
insert into Sales (employee_id, product_id, sales) values ('3', '2', '82');
insert into Sales (employee_id, product_id, sales) values ('3', '3', '82');
