"""
Created on Fri May 25 14:40:02 2018

@author: Nodar.Okroshiashvili
"""


import math
import os
import random
import re
import sys

    

N = int(input().strip())
f = []
for i  in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if emailID.endswith('@gmail.com'):
        f.append(firstName)
for name in sorted(f):
    print(name)
