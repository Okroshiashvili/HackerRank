
import re



def valid(s):
    if len(s) != 10:
        return 'Invalid'
    else:
        if  not re.search(r'.*[A-Z].*[A-Z].*', s):
            return 'Invalid'
        if not re.search(r'.*\d.*\d.*\d.*', s):
            return 'Invalid'
        if not re.search(r'[a-zA-Z\d]{10}', s):
            return 'Invalid'
        if re.search(r'(.).*\1', s):
            return 'Invalid'
        return 'Valid'

for _ in range(int(input())):
    s = input()
    print(valid(s))


