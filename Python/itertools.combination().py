"""
Created on Tue Nov 13 09:58:22 2018

@author: nokroshiashvili
"""



from itertools import combinations


S, k = input().split()

for i in range(1,int(k)+1):
    for j in combinations(sorted(S),i):
        print(''.join(j))



