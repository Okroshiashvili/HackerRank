"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np

N,M = list(map(int,input().split()))


  
A = np.array([[int(i) for i in input().split(' ')] for _ in range(N)])

print(np.prod(np.sum(A, axis=0)))


print(np.sum(A, axis=0))




