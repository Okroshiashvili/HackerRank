

select distinct(CITY) from STATION
where CITY REGEXP '^[aeiou]'
and CITY in (select CITY from STATION where CITY REGEXP '[aeiou]$');


