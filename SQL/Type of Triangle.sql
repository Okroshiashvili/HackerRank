


select if((A+ B) > C and (A + C)> B and (B + C) > A ,
            if(A = B and A = C and C=B,'Equilateral',
                if(A=B or B = C or A = C,'Isosceles','Scalene'))
        ,'Not A Triangle') TRIANGLES
from TRIANGLES;

