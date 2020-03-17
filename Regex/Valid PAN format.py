


import re


Regex_Pattern = r'^[A-Z]{0,5}\d{0,4}[A-Z]{1}$'


for _ in range(int(input())):
    if re.search(Regex_Pattern, input()):
        print("YES")
    else:
        print("NO")
