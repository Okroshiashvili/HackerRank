


import re

Regex_Pattern = r'\([+\-]?(90(\.0+)?|[1-8]\d(\.\d+)?|\d(\.\d+)?), [+\-]?(180(\.0+)?|1[0-7]\d(\.\d+)?|\d{2}(\.\d+)?|\d(\.\d+)?)\)'



r'\([\+-]?(90(\.0+)|[1-8]\d(\.[0-9]+)?|\d(\.[0-9]+)?), ([\+-]?(180(\.0+)?|1[0-7]\d|\d(\.[0-9]+)?|\d(\.[0-9]+)?)\)'



for i in range(int(input())):
    if re.match(Regex_Pattern, input()):
        print("Valid")
    else:
        print("Invalid")

