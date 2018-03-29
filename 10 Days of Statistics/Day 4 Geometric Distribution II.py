"""
Created on Wed Mar 28 10:49:07 2018

@author: Nodar.Okroshiashvili
"""

def geo_dist(n,p):
    return (1-p)**(n-1) * p

l =  list(map(int, input().split()))
p = l[0] / l[1]

n = int(input())


x = [geo_dist(i, p) for i in range(1,n+1)]

print(round(sum(x),3))

