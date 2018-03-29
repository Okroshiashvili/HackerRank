"""
Created on Tue Mar 20 10:01:56 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(' '.join(map(str, arr[::-1])))


