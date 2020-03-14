


import re



n = int(input())
text = "\n".join(input() for _ in range(n))
t = int(input())

for _ in range(t):
    print(len(re.findall(r'\B(%s)\B' % input().strip(),text)))

