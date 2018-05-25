"""
Created on Fri May 25 16:06:14 2018

@author: Nodar.Okroshiashvili
"""



import math
import os
import random
import re
import sys


T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    print(k - 1 if ((k - 1) | k) <= n else k - 2)
