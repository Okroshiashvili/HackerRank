"""
Created on Mon May 14 13:08:02 2018

@author: Nodar.Okroshiashvili
"""

import sys

n = int(input().strip())

a = list(map(int, input().strip().split(' ')))


def bubble_sort(arr):
    count_swap = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count_swap += 1
    print("Array is sorted in" + " " + str(count_swap) +" " + "swaps.")
    print("First Element:"+ " " + str(a[0]))
    print("Last Element:" + " " + str(a[-1]))


bubble_sort(a)


