"""
Created on Tue Sep  4 10:59:49 2018

@author: nokroshiashvili
"""

import sys


def summs(num,mul):
    num = num // mul
    return num * (num+1) * mul // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    print(summs(n,3) + summs(n,5) - summs(n,15))


#  HackerRank Solution
    


def s(n): return n*(n+1)/2
def r(n): return s(n/3)*3 + s(n/5)*5 - s(n/15)*15
print('\n'.join(str(r(int(input())-1)) for i in range(int(input()))))



