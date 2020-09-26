

import math
import os
import random
import re
import sys


# Complete the 'diagonalDifference' function below.

# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.


def diagonalDifference(arr):
    # Write your code here
    principal_diagonal = 0
    secondary_diagonal = 0

    for i in range(len(arr)):
        principal_diagonal += arr[i][i]
        secondary_diagonal += arr[i][len(arr) - i - 1]
    
    return abs(principal_diagonal - secondary_diagonal)
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



