CREATE DATABASE university;
USE university;

CREATE TABLE courses(
	id_course varchar(100),
	course_name varchar(100),
	course_schedule varchar(100),
	primary key(id_course)
);

SELECT * FROM courses;

