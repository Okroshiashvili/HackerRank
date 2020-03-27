
import re

p = ''

for _ in range(int(input())):
    p = p + input() + '\n'



for _ in range(int(input())):
    pattern = r'\b' + input() + r'\b'
    print(len(re.findall(pattern,p)))

