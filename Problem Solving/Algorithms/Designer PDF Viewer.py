

import math
import os
import random
import re
import sys


# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    letter_heights = [h[ord(i) - 97] for i in word]
    area = max(letter_heights) * len(letter_heights)

    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
