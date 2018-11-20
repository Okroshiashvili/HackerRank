"""
Created on Tue Nov 20 10:06:43 2018

@author: nokroshiashvili
"""



N = int(input())

stamp = set()
for i in range(N):
    stamp.add(input())
print(len(stamp))
    

# One line solution    
print(len(set([str(input()) for x in range(int(input()))])))

