"""
Created on Mon Mar 25 2019

@author: nokroshiashvili
"""


from collections import OrderedDict, Counter

n = int(input())


X = [input().split(' ') for _ in range(n)]


X = [j for i in X for j in i]

OrDic = OrderedDict(Counter(X))

print(len(OrDic.keys()))

print(*OrDic.values())


