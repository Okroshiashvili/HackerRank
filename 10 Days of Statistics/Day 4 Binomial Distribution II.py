"""
Created on Tue Mar 27 16:17:04 2018

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



p = float(input())
n = float(input())



result_1 = sum([b(i, n, p/100) for i in range(3)])
result_2 = sum([b(i, n, p/100) for i in range(2, int(n + 1))])

print(round(result_1,3))
print(round(result_2,3))

