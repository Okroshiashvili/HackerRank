"""
Created on Tue Apr 10 16:53:16 2018

@author: Nodar.Okroshiashvili
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string



s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

