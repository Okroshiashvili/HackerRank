


"""
The {x,y} tool will match between x and y (both inclusive) repetitions of character/character class/group.
"""


Regex_Pattern = r'^[\d]{1,2}[a-zA-Z]{3,}[.]{0,3}$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

