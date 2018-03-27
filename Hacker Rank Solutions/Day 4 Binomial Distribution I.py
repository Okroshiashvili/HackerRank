# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:25:45 2018

@author: Nodar.Okroshiashvili
"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

def combination(n,x):
    return factorial(n) / (factorial(x) * factorial(n-x))


def b(x, n, p):
    return combination(n,x) * p**x * (1-p)**(n-x)



y = float(input())
z = float(input())

odds = y / z

result = sum([b(i, 6, odds / (1 + odds)) for i in range(3,7)])

print(round(result,3))




"""
let p be the probability of being the boy = odds / (1 + odds)

"""
