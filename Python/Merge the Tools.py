"""
Created on Mon Jun  4 12:04:40 2018

@author: Nodar.Okroshiashvili
"""
from collections import OrderedDict

def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        print(''.join(OrderedDict.fromkeys(string[i:i+k]).keys()))


    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)   
    
    