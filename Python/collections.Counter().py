"""
Created on Wed Sep  5 09:37:19 2018

@author: nokroshiashvili
"""


from collections import Counter

X = int(input().strip()) # number of shoes
S = Counter(map(int,input().split())) # shoe sizes
N = int(input().strip()) # number of customers

income = 0

for i in range(N):
    size, price = map(int,input().split())
    
    if S[size]:
        income = income + price
        S[size] = S[size] - 1
        
print(income)

