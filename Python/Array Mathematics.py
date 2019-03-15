"""
Created on Fri Mar 15 11:07:11 2019

@author: Nodar Okroshiashvili
"""



import numpy as np


N, M = map(int, input().split())


A = np.array([input().split() for _ in range(N)], int)

B = np.array([input().split() for _ in range(N)], int)


print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')




