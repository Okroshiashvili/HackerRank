"""
Created on Wed Apr 11 10:37:05 2018

@author: Nodar.Okroshiashvili
"""

s = 'qA2'


a = []
b = []
c = []
d = []
e = []
for i in range(len(s)):
    a.append(s[i].isalnum())
    b.append(s[i].isalpha())
    c.append(s[i].isdigit())
    d.append(s[i].islower())
    e.append(s[i].isupper())
    

print(any(a))
print(any(b))
print(any(c))
print(any(d))
print(any(e))

#%%

# Second Solution


a = [a.isalnum() for a in s]
b = [b.isalpha() for b in s]
c = [c.isdigit() for c in s]
d = [d.islower() for d in s]
e = [e.isupper() for e in s]

print(any(a))
print(any(b))
print(any(c))
print(any(d))
print(any(e))



