"""
Created on Wed Apr 11 09:48:30 2018

@author: Nodar.Okroshiashvili
"""


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        x = int(sub_string in string[i:len(sub_string)+i:1])
        count += x
    return count 


string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)


