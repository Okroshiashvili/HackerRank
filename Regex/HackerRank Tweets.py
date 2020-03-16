


import re


Regex_Pattern = r'hackerrank'

N = int(input())

found = 0

for _ in range(N):
    if re.search(Regex_Pattern, input(), re.IGNORECASE):
        found += 1

print(found)


