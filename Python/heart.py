"""
Created on Wed Apr 11 13:45:21 2018

@author: Nodar.Okroshiashvili
"""



import math
c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))


