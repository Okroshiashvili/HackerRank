

select distinct(CITY) from STATION
where CITY RLIKE '^[^aeiou]'
and CITY in (select CITY from STATION where CITY RLIKE '[^aeiou]$');


