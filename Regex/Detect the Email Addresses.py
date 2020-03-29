


import re
import sys

p = sys.stdin.read()

Regex_Pattern = r'[\w\.]+@(?:\w+\.)+\w+'

emaillist=re.findall(Regex_Pattern, p)

print(';'.join(sorted(list(set(emaillist)))))

