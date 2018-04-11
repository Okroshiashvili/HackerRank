"""
Created on Tue Apr 10 13:52:59 2018

@author: Nodar.Okroshiashvili
"""

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

