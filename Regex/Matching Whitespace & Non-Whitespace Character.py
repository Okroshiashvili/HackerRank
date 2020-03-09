


"""
\s matches any whitespace character [ \r\n\t\f ].

\S matches any non-whitespace character.
"""



r"(\S{2}\s){2}\S{2}"

Regex_Pattern = r"\S{2}\s{1}\S{2}\s{1}\S{2}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

