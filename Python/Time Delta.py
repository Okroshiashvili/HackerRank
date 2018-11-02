"""
Created on Fri Nov  2 11:14:26 2018

@author: nokroshiashvili
"""

import datetime

#  Day dd Mon yyyy hh:mm:ss +xxxx
fmt = "%a %d %b %Y %H:%M:%S %z"

for i in range(int(input()) ):
    t1 = datetime.datetime.strptime( input().strip(), fmt )
    t2 = datetime.datetime.strptime( input().strip(), fmt )
    diff = datetime.timedelta.total_seconds(t1 - t2)
    print(abs(int(diff)))





###############################################################################

"""
Only Works for first test case

"""

import math
import os
import random
import re
import sys
import datetime
fmt = "%a %d %b %Y %H:%M:%S %z"
# Complete the time_delta function below.
def time_delta(t1, t2):
        x = datetime.datetime.strptime( t1, fmt )
        y = datetime.datetime.strptime( t2, fmt )
        diff = round(datetime.timedelta.total_seconds(x - y))
        return diff

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = str(time_delta(t1, t2))

        fptr.write(delta + '\n')

    fptr.close()
