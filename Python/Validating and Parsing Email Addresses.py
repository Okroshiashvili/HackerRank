

import re

pattern=r'(?<=<)[a-z][a-z0-9\.\_\-]*@[a-z]+\.[a-z]{1,3}(?=>)'

for _ in range(int(input())):
    s = input()
    if bool(re.search(pattern,s,re.IGNORECASE)):
        print(s)




