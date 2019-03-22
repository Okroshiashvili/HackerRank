"""
Created on Thu Mar 21 2019

@author: Nodar Okroshiashvili
"""




n , m = map(int, input().split())

initial_array = list(map(int, input().split()))


A = set(map(int, input().split()))

B = set(map(int, input().split()))


happiness = 0

for i in initial_array:
    happiness += ((i in A) - (i in B))
    
print(happiness)




