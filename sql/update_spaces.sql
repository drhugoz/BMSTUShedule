update professor
set "name" = replace(name, ' ', ' ')
where name like '% %'