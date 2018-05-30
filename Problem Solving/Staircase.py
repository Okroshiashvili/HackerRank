"""
Created on Wed May 30 10:22:44 2018

@author: Nodar.Okroshiashvili
"""


def staircase(n):
    for i in range(1,n+1):
        print((i*"#").rjust(n,' '), sep="\n")
              
              
if __name__ == '__main__':
    n = int(input())

    staircase(n)

             