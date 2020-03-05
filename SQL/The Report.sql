


SELECT if(Grade > 7,
         name,
         null),
         Grade,
         Marks
FROM Students, Grades
WHERE Marks
    BETWEEN Min_Mark
        AND Max_Mark
ORDER BY  Grade desc, Name;

