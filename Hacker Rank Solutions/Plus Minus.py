# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:51:50 2018

@author: Nodar.Okroshiashvili
"""



def plusminus(arr):
    positive = sum(x > 0 for x in arr) / len(arr)
    negative = sum(x < 0 for x in arr) / len(arr)
    zero = sum(x == 0 for x in arr) / len(arr)
    
    print(positive, negative, zero, sep="\n")

arr = (1, 2, -3, 0)
plusminus(arr)

