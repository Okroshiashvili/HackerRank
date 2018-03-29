"""
Created on Fri Mar 23 09:49:02 2018

@author: Nodar.Okroshiashvili
"""


n = int(input().strip())

binary = str("{0:b}".format(n)).split('0')
output = [len(i) for i in binary]
print(max(output))


