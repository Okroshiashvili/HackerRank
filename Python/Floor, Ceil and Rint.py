"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np

np.set_printoptions(sign=' ')

A = np.array(list(map(float, input().split())))


print(np.floor(A), np.ceil(A), np.rint(A), sep='\n')



