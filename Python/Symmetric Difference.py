"""
Created on Thu Nov  1 10:19:17 2018

@author: nokroshiashvili
"""




M, a = int(input()), set(map(int,input().split()))

N, b= int(input()), set(map(int,input().split()))

print(*sorted(a^b), sep='\n')

a.symmetric_difference(b)


# Symmetric Difference is XOR - exclusive OR problem
# This means we choose the set which contains elements either from first set or
# second set, but these elements must not be in both set not shoud be none
# Stated otherwise: either one, nor both nor none


