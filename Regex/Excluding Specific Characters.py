


"""
[^] - is negated character class that matches any character that is not in square brackets
"""




Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())




