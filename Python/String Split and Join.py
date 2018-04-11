"""
Created on Tue Apr 10 14:17:17 2018

@author: Nodar.Okroshiashvili
"""

line = "This is a string"


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


line = input()
result = split_and_join(line)
print(result

