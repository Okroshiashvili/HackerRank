

import re



Regex_Pattern = r'^[_.]\d+[a-zA-Z]*[_]?$'


for _ in range(int(input())):
    if re.search(Regex_Pattern, input()):
        print("VALID")
    else:
        print("INVALID")
