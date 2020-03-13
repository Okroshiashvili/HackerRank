


"""
regex_1(?!regex_2)

The negative lookahead (?!) asserts regex_1 not to be immediately followed by regex_2.
Lookahead is excluded from the match (do not consume matches of regex_2), but only assert whether a match is possible or not.
"""



Regex_Pattern = r"(.)(?!\1)"

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))



