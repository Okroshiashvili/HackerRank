"""
Created on Wed Mar 21 09:54:03 2018

@author: Nodar.Okroshiashvili
"""
# First Solution

n=int(input())
address_book=dict(input().split() for i in range(n))

for k,v in address_book.items():
    name=str(input()).lower()
    if name in address_book:
        print(name, address_book[name], sep="=")
    elif name not in address_book:
        print("Not found")


#%%
        
# Second Solution
        
        
n=int(input())
d=dict(input().split() for i in range(n))
names_list=[]

for i in range(n):
    name=str(input()).lower()
    if name in d:
        print('{}={}'.format(name,d[name]))
    else:
        print("Not found")

#%%
        
# Third Solution

n=int(input())
d={}

for i in range (0,n):
    str=input().split()
    d[str[0]]=str[1]
    
    
for z in range (n):
    z=input()
    if z in d :
        print(z+"="+d[z])
    else :
        print("Not found")        


