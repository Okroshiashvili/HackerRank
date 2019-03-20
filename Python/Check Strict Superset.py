"""
Created on Wed Mar 20 2019

@author: Nodar Okroshiashvili
"""





A = set(map(int, input().split()))


n = int(input())


result = []
  
for i in range(n):
    B = set(map(int, input().split()))
    result.append(A.issuperset(B))

print(all(result))






