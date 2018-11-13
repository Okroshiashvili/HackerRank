"""
Created on Tue Nov 13 10:54:42 2018

@author: nokroshiashvili
"""



from itertools import groupby


for i, j in groupby(str(input())):
    print('({}, {})'.format(len(list(j)),i), end=' ')

