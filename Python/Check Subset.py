"""
Created on Wed Mar 20 2019

@author: Nodar Okroshiashvili
"""



T = int(input())

result = []

for i in range(T):
    num_A = int(input())
    A = set(map(int, input().split()))
    num_B  = int(input())
    B = set(map(int, input().split()))
    result.append(A.issubset(B))

print(*(i for i in (result)), sep='\n')




# Second Solution


for _ in range(int(input())):
    _, a, _, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))




