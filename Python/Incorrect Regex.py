"""
Created on Tue Nov  6 11:16:10 2018

@author: nokroshiashvili
"""


import re

for i in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)




