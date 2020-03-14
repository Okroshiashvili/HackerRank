

import re
import sys


Regex_Pattern = r'<\s*(\w+)'

print(";".join(sorted(set(re.findall(Regex_Pattern, sys.stdin.read())))))
