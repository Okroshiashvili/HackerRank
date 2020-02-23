

select salary*months as earnings, count(*) from EMPLOYEE
group by earnings
order by earnings
desc limit 1;

