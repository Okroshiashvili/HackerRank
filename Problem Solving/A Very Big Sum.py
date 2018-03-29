"""
Created on Thu Mar 22 13:36:18 2018

@author: Nodar.Okroshiashvili
"""

n = int(input())

ar = list(map(int, input().rstrip().split()))


def aVeryBigSum(n, ar):
    x = sum(ar)
    return x


result = aVeryBigSum(n, ar)

#%%

# Second solution

def aVeryBigSum(n, ar):
    from functools import reduce
    x = reduce(lambda x, y : x + y, ar)
    return x

result = aVeryBigSum(n, ar)

