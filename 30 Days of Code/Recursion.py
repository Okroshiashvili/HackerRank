"""
Created on Thu Mar 22 10:07:27 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())



def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result



result = factorial(n)

