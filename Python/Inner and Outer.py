"""
Created on Fri Mar 15 14:10:05 2019

@author: Nodar Okroshiashvili
"""


import numpy as np

A = np.array([int(i) for i in input().split()])

B = np.array([int(i) for i in input().split()])


print(np.inner(A,B),np.outer(A,B), sep='\n')




