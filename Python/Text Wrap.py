"""
Created on Wed Apr 11 13:55:48 2018

@author: Nodar.Okroshiashvili
"""


import textwrap


      
def wrap(string, max_width):
    return (textwrap.fill(string,width=max_width))



string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width=4


print(wrap(string,max_width))


