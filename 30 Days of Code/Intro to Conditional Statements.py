"""
Created on Fri Mar 16 17:02:35 2018

@author: Nodar.Okroshiashvili
"""

N = int(input().strip())

if N % 2 != 0:  # this is even
    print("Weird")
elif N % 2 == 0 and N in range(2,6):
    print("Not Weird")
elif N % 2 == 0 and N in range(6, 21):
    print("Weird")
elif N % 2 ==0 and N > 20:
    print("Not Weird")
else:
    pass

