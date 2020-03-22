


import re

Regex_Pattern_1 = r'<((\w+).*?)>'
Regex_Pattern_2 = r'\s(\w+)='

d = {}


for i in  range(int(input())):
    for t in re.findall(Regex_Pattern_1, input()):
        attrs = [x.group(1) for x in re.finditer(Regex_Pattern_2, t[0])]
        if t[1] in d:
            d[t[1]].update(attrs)
        else:
            d[t[1]] = set(attrs)


print(*sorted(["{}:{}".format(k,",".join(sorted(v))) for k,v in d.items()]), sep="\n")


