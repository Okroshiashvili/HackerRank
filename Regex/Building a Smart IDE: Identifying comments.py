



import re
import sys


text = sys.stdin.read()


Regex_Pattern = r'(?s)(?m)(//.*?$|/\*.*?\*/)'


print("\n".join(re.sub(r"\n\s+", "\n", comment) for comment in re.findall(Regex_Pattern, text)))


