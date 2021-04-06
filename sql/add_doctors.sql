DROP TABLE doctor_schedule;
DROP TABLE doctor;

CREATE TABLE doctor
(
	"id" integer PRIMARY KEY NOT NULL,
	"name" character varying NOT NULL,
	spec character varying,
	office character varying
);

CREATE TABLE doctor_schedule
(
	"id" integer PRIMARY KEY NOT NULL,
	doctor_id integer REFERENCES doctor(id),
	"date" character varying,
	"time" character varying
);

COPY doctor FROM 'C:\Progs\CompNetWorks\Project\MarusyaBMSTUScheduleSkill\doctors.csv' DELIMITER ';';
COPY doctor_schedule FROM 'C:\Progs\CompNetWorks\Project\MarusyaBMSTUScheduleSkill\dates.csv' DELIMITER ';';