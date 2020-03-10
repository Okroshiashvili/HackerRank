


"""
A hyphen (-) inside a character class specifies a range of characters
where the left and right operands are the respective lower and upper bounds of the range.
[a-z]
"""


Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())




