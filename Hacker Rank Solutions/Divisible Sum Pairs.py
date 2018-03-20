# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 17:25:54 2018

@author: Nodar.Okroshiashvili
"""


from itertools import combinations as cmn

y = [1, 2, 3]
x = list(cmn(y, 2))


for i in range(len(x)):
    for j in range(i):
        suma = x[i][j] + x[i][j+1]
    total_suma = list(suma)
    
    
    
 #%%
       
suma = [(a + b) for (a, b) in zip(y[:-1], y[1:])]

"""
ეს შეიძლება გამომადგეს

"""



#%%
suma = 0
for pair in x:
    print(pair)
    sum(i for i, _ in x)
    suma = suma + pair[0]



"""
დასამთავრებელია

"""




