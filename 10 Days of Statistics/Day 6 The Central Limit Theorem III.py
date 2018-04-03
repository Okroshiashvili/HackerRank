"""
Created on Tue Apr  3 13:36:39 2018

@author: Nodar.Okroshiashvili
"""


n = float(input())
mu = float(input())
sigma = float(input())
gamma = float(input())
z = float(input())


A = mu - (z * (sigma / n ** 0.5))
B = mu + (z * (sigma / n ** 0.5))


print(round(A,2))   
print(round(B,2))



