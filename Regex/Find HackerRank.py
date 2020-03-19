


import re



for _ in range(int(input())):
    value = input().strip()
    if re.search(r'^(hackerrank)$', value):
        print(0)
    elif re.search(r'^hackerrank', value):
        print(1)
    elif re.search(r'hackerrank$', value):
        print(2)
    else:
        print(-1)


