

import re


for i in range(int(input())):
    print(re.sub(r' (&&|\|\|)(?= )', lambda m: ' and' if m.group() == ' &&' else ' or', input()))


    