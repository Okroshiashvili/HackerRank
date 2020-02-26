


select round(S.LAT_N,4) median from STATION S
where (select count(Lat_N) 
       from STATION where Lat_N < S.LAT_N ) = (select count(Lat_N) 
                                               from STATION where Lat_N > S.LAT_N)


