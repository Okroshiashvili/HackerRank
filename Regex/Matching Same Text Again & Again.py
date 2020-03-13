


"""

\group_number

This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.
"""



Regex_Pattern = r'^([a-z]\w\s\W\d\D[A-Z][a-zA-Z][aeiouAEIOU]\S)\1$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


