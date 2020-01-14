
import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


decoded_string = []

# char is a tuple of each input column
for char in zip(*matrix):
    # extend adds iterable at the end of the list
    decoded_string.extend(char)

# join joins the each element of a list
decoded_string = ''.join(decoded_string)

# regex pattern for replacement with spaces
print(re.sub(r'\b[^a-zA-z0-9]+?\b', ' ', decoded_string))

