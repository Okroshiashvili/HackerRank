"""
Created on Wed Mar 13 09:33:04 2019

@author: Nodar Okroshiashvili
"""



# Number of elements in set A
n = int(input())


# Set A
A = set(map(int, input().split()))

# The number of other sets
N = int(input())




for i in range(N):
    c, *args = map(str, input().split())
    getattr(A,c) (set(map(int, input().split())))

print(sum(A))



