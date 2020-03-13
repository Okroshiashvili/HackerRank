


"""
(?<=regex_2)regex_1

The positive lookbehind (?<=) asserts regex_1 to be immediately preceded by regex_2.
Lookbehind is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
"""



Regex_Pattern = r"(?<=[13579])\d"

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))



