# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:41:55 2018

@author: Nodar.Okroshiashvili
"""


def prime(n):
    if n > 2:
        if n % 2 == 0:
            return "Not prime"
        else:
            if n % int(n**0.5) == 0:
                return "Not prime"
            for i in range(3, int(n**0.5)):
                if n % i == 0:
                    return "Not prime"
                else:
                    i += 2
            return "Prime"
    elif n == 2:
        return "Prime"
    return "Not prime"
                    



T = int(input())
for i in range(T):
    number = int(input())
    print(prime(number))
    
   
       