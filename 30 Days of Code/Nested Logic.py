"""
Created on Fri May 25 13:09:53 2018

@author: Nodar.Okroshiashvili
"""

a_D, a_M, a_Y = [int(x) for x in input().split(' ')]
e_D, e_M, e_Y = [int(x) for x in input().split(' ')]

if a_D <= e_D and a_M <= e_M and a_Y <= e_Y:
    print(0)
elif a_D > e_D and (a_M, a_Y) == (e_M, e_Y):
    print(15 * (a_D - e_D)) 
elif a_M > e_M:
    if a_Y > e_Y:
        print(10000)
    elif a_M > e_M and a_Y < e_Y:
        print(0)
    else:
        print(500 * (a_M - e_M))      
elif a_Y > e_Y:
    print(10000)       
else:
    print(0)
