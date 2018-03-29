"""
Created on Thu Mar 29 10:20:55 2018

@author: Nodar.Okroshiashvili
"""





from math import erf

def phi(x, mu, sigma):
    return (1.0 + erf((x - mu) / (sigma * (2.0**0.5)))) / 2.0



mu, sigma = list(map(float,input().strip().split(" ")))
x_0 = float(input())
x_1, x_2 = list(map(float,input().strip().split(' ')))

print(round(phi(x_0, mu, sigma),3))
print(round(phi(x_2, mu,sigma) - phi(x_1, mu,sigma),3))

