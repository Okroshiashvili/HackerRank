"""
Created on Fri Mar 15 10:06:08 2019

@author: Nodar Okroshiashvili

"""



import numpy as np


N = int(input())

# Matrix A   
A = [[float(i) for i in input().split(' ')] for _ in range(N)]


print(np.linalg.det(A))





