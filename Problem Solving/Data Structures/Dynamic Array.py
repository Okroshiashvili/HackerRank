

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):

    sequence_list = [[] for _ in range(n)]
    last_answer = 0
    result = []
    
    for query in queries:
        if query[0] == 1:
            sequence = (query[1] ^ last_answer) % n
            sequence_list[sequence].append(query[2])
        else:
            sequence = (query[1] ^ last_answer) % n
            last_answer = sequence_list[sequence][query[2] % len(sequence_list[sequence])]
            result.append(last_answer)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

