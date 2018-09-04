"""
Created on Tue Sep  4 10:22:20 2018

@author: nokroshiashvili
"""


from itertools import permutations


s,n = input().split()


x = sorted(list(permutations(s,int(n))))

for i in x:
    print(*i,sep='')


