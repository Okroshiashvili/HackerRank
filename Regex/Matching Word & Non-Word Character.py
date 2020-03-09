


"""
\w - match any word character, which include (a-z, A-Z, 0-9) and underscore.

\W - match non-word characters

"""



Regex_Pattern = r"(\w{3}\W){1}\w{10}\W{1}\w{3}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


