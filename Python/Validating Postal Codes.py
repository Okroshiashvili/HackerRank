


regex_integer_in_range = r"^([1-9][0-9][0-9][0-9][0-9][0-9])$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


'''
r"(\d)(?=\d\1)" - uses lookahead


(\d): Match and capture a digit in group #1

(?=: Start lookahead

    \d: Match any digit

    \1: Back-reference to captured group #1

): End lookahead


We can use Python List Comprehension if needed
to find alternating repetitive digit pair




s = '552523'

[a for a, b in zip(s, s[2:]) if a == b]



'''



import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)






