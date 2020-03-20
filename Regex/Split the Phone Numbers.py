


import re


Regex_Pattern = r'(\d+)$'


for _ in range(int(input())):
    match = re.findall(Regex_Pattern, input())
    print("CountryCode={},LocalAreaCode={},Number={}".format(match[0], match[1], match[2]))


