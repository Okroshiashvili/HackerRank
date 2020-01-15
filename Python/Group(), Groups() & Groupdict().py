

import re


s = str(input())

m = re.search(r'([a-zA-Z\d])\1+', s)



print(m.group(1) if m else -1)


