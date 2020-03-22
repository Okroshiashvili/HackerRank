


import re

str = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    print(len(re.findall(input()[:-2]+'[zs]e', str)))
