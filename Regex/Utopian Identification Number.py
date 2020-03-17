


import re


Regex_Pattern = r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}$'


for _ in range(int(input())):
    if re.search(Regex_Pattern, input()):
        print("VALID")
    else:
        print("INVALID")
