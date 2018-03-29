"""
Created on Mon Mar 19 12:06:58 2018

@author: Nodar.Okroshiashvili
"""

n = int(input().strip())

x = [print("{} x {} = {}".format(n, i, n*i)) for i in range(1, 11)]



#%%
    
# Second Solution

n = int(input().strip())

for i in range(1,11):
    print("{} x {} = {}".format(n, i, (n*i)))

	
