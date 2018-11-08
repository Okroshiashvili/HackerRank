"""
Created on Thu Nov  8 10:16:31 2018

@author: nokroshiashvili
"""



from collections import OrderedDict

N = int(input())   # Number of items

ord_dict = OrderedDict()   # Ordered Dict to store data

for i in range(N):
    item, price = input().rsplit(' ', 1)   # splits string from right to left
    ord_dict[item] = ord_dict.get(item, 0) + int(price)

[print(item, price) for item, price in ord_dict.items()]


# Second way to print the results
for item, price in ord_dict.items():
    print(item, price)





