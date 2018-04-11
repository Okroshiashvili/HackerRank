"""
Created on Thu Apr  5 13:08:15 2018

@author: Nodar.Okroshiashvili
"""


n = int(input())
arr = list(map(int, input().split()))

maximum = max(arr)
while max(arr) == maximum:
    arr.remove(max(arr))

print(max(arr))



x = sorted(list(set(arr)))[-2]
