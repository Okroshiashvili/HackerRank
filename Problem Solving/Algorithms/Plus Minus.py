

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_ratio = sum(x > 0 for x in arr) / len(arr)
    negative_ratio = sum(x < 0 for x in arr) / len(arr)
    zero_ratio = sum(x == 0 for x in arr) / len(arr)

    print(positive_ratio, negative_ratio, zero_ratio, sep="\n")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
