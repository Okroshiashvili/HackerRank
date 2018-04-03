"""
Created on Fri Mar 30 15:41:29 2018

@author: Nodar.Okroshiashvili
"""

max_weight = float(input())
x = float(input())
mu = float(input())
sigma = float(input())



from math import erf

def phi(x, mu, sigma):
    return (1.0 + erf((x - mu) / (sigma * (2.0**0.5)))) / 2.0


Z = (max_weight - mu * x) / (x**0.5 * sigma)

print(round(phi(Z, 0, 1),4))


