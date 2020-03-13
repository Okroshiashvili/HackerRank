


"""
Backreference to a capturing group that match nothing is different from backreference
to a capturing group that did not participate in the match at all.
"""



Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())




