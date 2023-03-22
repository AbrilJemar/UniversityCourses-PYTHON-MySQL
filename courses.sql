CREATE DATABASE university;
USE university;

CREATE TABLE courses(
	id_course varchar(100),
    	course_name varchar(100),
    	course_schedule varchar(100),
    	primary key(id_course)
);

INSERT INTO courses(id_course, course_name, course_schedule) VALUES ("K1234", "Mathematical analysis", "Monday from 7:00 p.m. to 11:00 p.m.");
INSERT INTO courses(id_course, course_name, course_schedule) VALUES ("K4321", "Biology", "Thursday from 7:00 p.m. to 11:00 p.m.");
INSERT INTO courses(id_course, course_name, course_schedule) VALUES ("56783", "Economy", "Wednesday from 7:00 p.m. to 11:00 p.m.");

SELECT * FROM courses;

