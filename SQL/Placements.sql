


SELECT S.name
FROM Students S
JOIN Friends F
    ON S.ID = F.ID
JOIN Packages P
    ON F.ID = P.ID
JOIN Packages P2
    ON F.Friend_ID = P2.ID
WHERE P.Salary < P2.Salary
ORDER BY  P2.Salary;

