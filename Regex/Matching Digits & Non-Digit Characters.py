


"""
\d - match any digit [0-9]

\D - match any character that is not a digit

"""



Regex_Pattern = r"(\d{2}\D){2}\d{4}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


