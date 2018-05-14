"""
Created on Mon May 14 11:26:18 2018

@author: Nodar.Okroshiashvili
"""

import sys


S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
    

