"""
Created on Tue Nov  6 11:06:26 2018

@author: nokroshiashvili
"""




T = int(input())


for i in range(int(input())):
    try:
        a,b = map(int,input().split())
        print(a // b)
    except BaseException as e:
        print('Error Code:', e)

