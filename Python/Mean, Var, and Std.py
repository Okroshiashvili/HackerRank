"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np

np.set_printoptions(legacy='1.13')

N,M = list(map(int,input().split()))


  
A = np.array([[int(i) for i in input().split(' ')] for _ in range(N)])



print(np.mean(A, axis=1), np.var(A, axis=0), np.std(A), sep='\n')



