temp_db = """
SELECT "group".name AS GroupName, subject.name AS SubjectName, auditorium.name AS AudName, professor.name AS ProfName, lesson.weekday, lesson.repeat_type, lesson.number
INTO TEMPORARY GroupTempTable
FROM lesson JOIN "group" ON lesson.group_id = "group".id
			JOIN subject ON lesson.subject_id = subject.id
			JOIN lesson_type ON lesson.type_id = lesson_type.id
			JOIN professor ON lesson.professor_id = professor.id
			JOIN lesson_auditorium ON lesson.id = lesson_auditorium.lesson_id
			JOIN auditorium ON auditorium_id = auditorium.id;

ALTER TABLE GroupTempTable
ADD COLUMN DayName CHARACTER VARYING,
ADD COLUMN BeginningTime CHARACTER VARYING,
ADD COLUMN EndingTime CHARACTER VARYING;

UPDATE GroupTempTable
SET DayName = 'Понедельник'
WHERE weekday = 0;

UPDATE GroupTempTable
SET DayName = 'Вторник'
WHERE weekday = 1;

UPDATE GroupTempTable
SET DayName = 'Среда'
WHERE weekday = 2;

UPDATE GroupTempTable
SET DayName = 'Четверг'
WHERE weekday = 3;

UPDATE GroupTempTable
SET DayName = 'Пятница'
WHERE weekday = 4;

UPDATE GroupTempTable
SET DayName = 'Суббота'
WHERE weekday = 5;

UPDATE GroupTempTable
SET BeginningTime = '8:30', EndingTime = '10:05'
WHERE number = 0;

UPDATE GroupTempTable
SET BeginningTime = '10:15', EndingTime = '11:50'
WHERE number = 1;

UPDATE GroupTempTable
SET BeginningTime = '12:00', EndingTime = '13:35'
WHERE number = 2;

UPDATE GroupTempTable
SET BeginningTime = '13:50', EndingTime = '15:25'
WHERE number = 3;

UPDATE GroupTempTable
SET BeginningTime = '15:40', EndingTime = '17:15'
WHERE number = 4;

UPDATE GroupTempTable
SET BeginningTime = '17:25', EndingTime = '19:00'
WHERE number = 5;

UPDATE GroupTempTable
SET BeginningTime = '19:10', EndingTime = '20:45'
WHERE number = 6;
"""
