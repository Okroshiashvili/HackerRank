"""
Created on Tue Mar 26 2019

@author: Nodar Okroshiashvili
"""


from collections import deque



N = int(input())

d = deque()

for i in range(N):
    c, *args = map(str, input().split())
    getattr(d,c) (*(int(x) for x in args))
    
print(*d)




