"""
Created on Tue Sep  4 09:55:53 2018

@author: nokroshiashvili
"""

from itertools import product


A = list(map(int,input().split()))
B  = list(map(int,input().split()))

print(*product(A,B))

