


"""
[ ] - matches only one out of several characters placed inside the square brackets.

"""



Regex_Pattern = r'^[1-3][0-2][xs0][03Aa][xsu][.,]'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())




