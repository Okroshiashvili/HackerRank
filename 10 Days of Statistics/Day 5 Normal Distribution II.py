"""
Created on Thu Mar 29 16:14:12 2018

@author: Nodar.Okroshiashvili
"""


from math import erf

def phi(x, mu, sigma):
    return (1.0 + erf((x - mu) / (sigma * (2.0**0.5)))) / 2.0


mu, sigma = list(map(float,input().strip().split(" ")))

passed = float(input())
failed = float(input())


print(round(100 - phi(passed, mu, sigma)*100,2))

print(round(100 - phi(failed, mu, sigma)*100,2))
print(round(phi(failed, mu, sigma)*100, 2))


#%%


# Second Solution

import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))

