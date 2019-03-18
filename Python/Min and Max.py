"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np

N,M = list(map(int,input().split()))


  
A = np.array([[int(i) for i in input().split(' ')] for _ in range(N)])


print(np.max(np.min(A, axis=1)))

