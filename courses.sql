CREATE DATABASE university;
USE university;

CREATE TABLE courses (
	id int auto_increment PRIMARY KEY,
	id_course varchar(100),
	course_name varchar(100),
    	course_schedule varchar(100),
    	period varchar(100)
);


INSERT INTO courses(id_course, course_name, course_schedule, period) VALUES ("K1234", "Mathematical analysis", "Monday from 7:00 p.m. to 11:00 p.m.", "first semester 2023");
INSERT INTO courses(id_course, course_name, course_schedule, period) VALUES ("K4321", "Biology", "Thursday from 7:00 p.m. to 11:00 p.m.", "Annual 2022");
INSERT INTO courses(id_course, course_name, course_schedule, period) VALUES ("56783", "Economy", "Wednesday from 7:00 p.m. to 11:00 p.m.", "Annual 2023");

SELECT * FROM courses;

