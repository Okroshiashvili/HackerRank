# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:33:09 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())
X = list(map(int, input().strip().split(' ')))
F = list(map(int, input().strip().split(' ')))

XF = list([[i] * j for i, j in zip(X,F)])

S = [i for j in XF for i in j]

S = sorted(S)

def interquartile(S): # Aq unda chavwero S romelic aris X da F naerti listi
    median = (S[len(S) // 2] + S[-(len(S) // 2 + 1)]) // 2
    if len(S) % 2 == 0:
        L = S[: len(S) // 2]
        U = S[len(S) // 2 :]
    else:
        L = S[:S.index(median)+1]
        U = S[S.index(median)+2:]
        
    Q1 = (L[len(L) // 2] + L[-(len(L) // 2 + 1)]) / 2
    Q3 = (U[len(U) // 2] + U[-(len(U) // 2 + 1)]) / 2
    output = Q3 - Q1
    print(output)


interquartile(S)
