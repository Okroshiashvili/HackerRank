"""
Created on Wed Mar 21 11:58:31 2018

@author: Nodar.Okroshiashvili
"""


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def pickingNumbers(a):
    x = max((a.count(i) + a.count(i+1) for i in a))
    return x

    
pickingNumbers(a)



#%%

# Second Solution

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


def pickingNumbers(a):
    set_ = set(a)  
    a_ = [a.count(each) + a.count(each+1) for each in set_]
    return max(a_)

pickingNumbers(a)

