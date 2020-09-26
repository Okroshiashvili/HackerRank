

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maximum_sum = sum(arr) - min(arr)
    minimum_sum = sum(arr) - max(arr)

    print(minimum_sum, maximum_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
