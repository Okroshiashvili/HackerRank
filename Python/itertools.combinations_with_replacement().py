"""
Created on Tue Nov 13 10:42:00 2018

@author: nokroshiashvili
"""



from itertools import combinations_with_replacement

S, k = input().split()

for i in combinations_with_replacement(sorted(S),int(k)):
        print(''.join(i))





