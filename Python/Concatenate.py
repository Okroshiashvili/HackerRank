"""
Created on Tue Mar 19 2019

@author: Nodar Okroshiashvili
"""



import numpy as np



N, M, P = map(int, input().split())


  
A = np.array([[int(i) for i in input().split(' ')] for _ in range(N)], int)

B = np.array([[int(i) for i in input().split(' ')] for _ in range(M)], int)


print(np.concatenate((A,B), axis=0))


