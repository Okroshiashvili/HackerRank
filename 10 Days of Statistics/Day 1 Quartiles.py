"""
Created on Fri Mar 23 13:25:28 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())
X = list(map(int, input().strip().split(' ')))
X = sorted(X)


def quartiles(X): 
    median = (X[n // 2] + X[-(n // 2 + 1)]) // 2
    if n % 2 == 0:
        L = X[: n // 2]
        U = X[n // 2 :]
    else:
        L = X[:X.index(median)]
        U = X[X.index(median)+1:]
        
    Q1 = (L[len(L) // 2] + L[-(len(L) // 2 + 1)]) // 2
    Q2 = median
    Q3 = (U[len(U) // 2] + U[-(len(U) // 2 + 1)]) // 2
    print(Q1, Q2, Q3, sep='\n')


quartiles(X)


