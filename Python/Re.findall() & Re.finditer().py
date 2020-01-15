


import re

vowels = 'aeiou'

consonants = 'qwrtypsdfghjklzxcvbnm'


pattern = '(?<=[' + consonants + '])([' + vowels + ']{2,})[' + consonants + ']'

match = re.findall(pattern, input(), re.IGNORECASE)

# print(*match, sep='\n' if match else -1)


if match:
    print(*match, sep='\n')
else:
    print('-1')


