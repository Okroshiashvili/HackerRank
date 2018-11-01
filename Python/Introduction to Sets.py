"""
Created on Thu Nov  1 10:01:27 2018

@author: nokroshiashvili
"""


def average(array):
    x = set(array)
    return sum(x) / len(x)

    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    result = average(arr)
    print(result)
    
    
    