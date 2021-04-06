INSERT INTO building VALUES
(2, 'ГЗ'),
(3, 'СМ'),
(4, 'Энерго'),
(5, 'МТ');

UPDATE auditorium
SET building_id = 2
where "name" LIKE '%ю';

UPDATE auditorium
SET building_id = 2
WHERE "name" SIMILAR TO '%(1|2|3|4|5|6|7|8|9|0)';

UPDATE auditorium
SET building_id = 3
where "name" LIKE '%м';

UPDATE auditorium
SET building_id = 4
where "name" LIKE '%э';

UPDATE auditorium
SET building_id = 5
where "name" LIKE '%мт';