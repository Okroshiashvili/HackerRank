


import re

regex_pattern_ipv4 = r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
regex_pattern_ipv6 = r'^([0-9a-f]{0,4}:){7}[0-9a-f]{0,4}$'


for _ in range(int(input())):

    s = input()

    if re.match(regex_pattern_ipv4, s, re.I): 
        print("IPv4")
    elif re.match(regex_pattern_ipv6,s, re.I):
        print("IPv6")
    else: 
        print("Neither")





