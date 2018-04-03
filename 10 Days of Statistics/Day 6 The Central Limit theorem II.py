"""
Created on Tue Apr  3 13:12:29 2018

@author: Nodar.Okroshiashvili
"""

tickets = float(input())
students = float(input())
mu = float(input())
sigma = float(input())



from math import erf

def phi(x, mu, sigma):
    return (1.0 + erf((tickets - (mu * students)) / ((sigma * (students**0.5))* (2.0**0.5)))) / 2.0


print(round(phi(students,mu,sigma),4))


