"""
Created on Wed Mar 28 14:11:00 2018

@author: Nodar.Okroshiashvili
"""


def factorial(k):
    return 1 if k == 1 else k * factorial(k-1)

from math import exp

def poisson(l,k):
    return (l**k * exp(-l)) / factorial(k)

l = float(input())
k = float(input())

print(round(poisson(l,k),3))
