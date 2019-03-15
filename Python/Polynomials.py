"""
Created on Fri Mar 15 14:24:26 2019

@author: Nodar Okroshiashvili
"""



import numpy as np


p = np.array([float(i) for i in input().split()])

x = float(input())



print(np.polyval(p,x))






