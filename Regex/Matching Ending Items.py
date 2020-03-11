


"""
The $ (dollar sign) boundary matcher matches an occurrence of a character/character class/group at the end of a line.
"""



Regex_Pattern = r'^[a-zA-Z]*s$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
