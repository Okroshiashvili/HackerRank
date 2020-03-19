


import re


Regex_Pattern = r'^[Hh][Ii]\s[^Dd].*'


N = int(input())


for _ in range(N):
    value = input().strip()
    if re.search(Regex_Pattern, value):
        print(value)
    else:
        pass

