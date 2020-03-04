

SELECT C.company_code, 
       C.founder,
       COUNT(DISTINCT L.lead_manager_code),
       COUNT(DISTINCT S.senior_manager_code),
       COUNT(DISTINCT M.manager_code),
       COUNT(DISTINCT E.employee_code)
FROM Company as C,
     Lead_Manager as L,
     Senior_Manager as S,
     Manager as M,
     Employee as E 
WHERE E.manager_code = M.manager_code 
AND M.senior_manager_code = S.senior_manager_code
AND L.lead_manager_code = S.lead_manager_code
AND C.company_code = L.company_code
GROUP By C.company_code, C.founder
ORDER By C.company_code;


