"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np

N = int(input())

  
A = np.array([[int(i) for i in input().split(' ')] for _ in range(N)])

B = np.array([[int(i) for i in input().split(' ')] for _ in range(N)])


print(np.dot(A,B))





