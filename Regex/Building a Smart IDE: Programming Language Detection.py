


import re
import sys

source = ''.join(sys.stdin.readlines())

if 'java' in source:
    print("Java")
elif '#include' in source:
    print("C")
else:
    print("Python")
