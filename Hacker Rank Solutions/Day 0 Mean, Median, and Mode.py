# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:51:49 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))


def describe_stat(arr):
    arr = sorted(arr)
    mean = sum(arr) / n
    median = (arr[n // 2] + arr[-(n // 2 + 1)]) /2
    mode = max(arr, key=arr.count)
    print(mean, median, mode, sep='\n')


describe_stat(arr)


