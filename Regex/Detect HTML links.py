


import re

Regex_Pattern = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'



for _ in range(int(input())):
    html = input()
    res = re.findall(Regex_Pattern, html)
    for link, title in res:
        print("{},{}".format(link, title.strip()))

