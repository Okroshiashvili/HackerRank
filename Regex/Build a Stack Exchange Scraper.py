


import re, sys

regex = re.compile(r'/questions/(\d+).*?>(.+?)<.*?ativetime">(.+?)</s', re.DOTALL)

print('\n'.join([';'.join(x) for x in regex.findall(sys.stdin.read())]))

