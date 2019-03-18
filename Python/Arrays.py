"""
Created on Mon Mar 18 2019

@author: Nodar Okroshiashvili
"""



import numpy as np


A = np.array(list(map(int, input().split())))

print(np.array(A[::-1],float))




#        Second Solution



import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr[::-1],float)
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)





