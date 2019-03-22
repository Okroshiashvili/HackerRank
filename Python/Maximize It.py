"""
Created on Thu Mar 21 2019

@author: Nodar Okroshiashvili
"""

from itertools import product

K, M = map(int, input().split())


N = [list(map(int, input().split()))[1:] for _ in range(K)]


# The answer
print(max((sum(i**2 for i in j) % M for j in product(*N))))

# Explanation
"""
First time, itertools product makes all combination of input arrays
and star * unpacks this all combinations. Particularlly, this
combinations are cartesian product.

product(A, B) is equivalent to ((x,y) for x in A for y in B)


After that, j returns tuple in this way (5, 7, 5)

We now want to run inside this tuple square each element and sum them up.
That's what inside for loop does

After that we have all the square elements sum, we choose maximum among them


"""


# See the mechanics of itertools product
x = list(product(*N))


# Itertools product example
https://www.hackerrank.com/challenges/itertools-product/problem
     
