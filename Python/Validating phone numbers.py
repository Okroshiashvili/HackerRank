

import re

for i in range(int(input())):
    x=input()

    if len(x)==10 and re.match('^[789]\d{9}',x):
        print('YES')
    else:
        print('NO')



