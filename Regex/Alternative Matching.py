


"""
Alternations, denoted by the | character, match a single item out of several possible items separated by the vertical bar.
When used inside a character class, it will match characters;
when used inside a group, it will match entire expressions (i.e., everything to the left or everything to the right of the vertical bar).
We must use parentheses to limit the use of alternations.

"""





Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())




