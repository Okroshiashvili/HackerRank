


import re
import sys

html = sys.stdin.read()

Regex_Pattern = r'https?:\/\/(?:www\.|ww\d\.)?([\w\.-]+\.[a-zA-Z]*)'

matches = sorted(list(set(re.findall(Regex_Pattern,html))))

print(";".join(matches))

