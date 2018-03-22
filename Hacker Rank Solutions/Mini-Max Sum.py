# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:47:24 2018

@author: Nodar.Okroshiashvili
"""

arr = list(map(int, input().rstrip().split()))


def miniMaxSum(arr):
    suma = sum(arr)
    minimum = suma - max(arr)
    maximum = suma - min(arr)
    print(minimum, maximum)
    
    
miniMaxSum(arr)
