"""
Created on Wed Mar 28 10:12:54 2018

@author: Nodar.Okroshiashvili
"""


def geo_dist(n,p):
    return (1-p)**(n-1) * p

l =  list(map(int, input().split()))
p = l[0] / l[1]

n = int(input())


print(round(geo_dist(n,p),3))
