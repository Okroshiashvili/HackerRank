# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:51:39 2018

@author: Nodar.Okroshiashvili
"""


N = int(input().strip())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))

def weighted_mean(X, W):
    output = round(sum([i * j for i, j in zip(X,W)]) / sum(W),1)
    print(output)

weighted_mean(X,W)


