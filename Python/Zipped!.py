"""
Created on Tue Mar 19 2019

@author: Nodar Okroshiashvili
"""



N, X = map(int, input().split())


Marks = [list(map(float, input().split())) for _ in range(X)]


[print(sum(i)/len(i)) for i in zip(*Marks)]




