"""
Created on Mon Nov 19 10:07:35 2018

@author: nokroshiashvili
"""

from itertools import combinations

N = int(input())

S = input().strip().split()

K = int(input())


x = ['a' in i for i in combinations(S,K)]

print(round(sum(x) / len(x),3))



# x is a list of True/False values, where True means that letter 'a' uccurred 
# at least one time in our two element set. False means opposite

# Our task is to find probability of occurring letter 'a' in all sets
# This means we have to count how many time our set of two elements contains a
# and divide this number by the length of this combination


