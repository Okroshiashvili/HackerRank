"""
Created on Wed Mar 20 2019

@author: Nodar Okroshiashvili
"""



N, list_int = int(input()), input().split()

print(all(int(i) > 0 for i in list_int) and any(j == j[::-1] for j in list_int))



