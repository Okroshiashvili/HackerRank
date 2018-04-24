"""
Created on Tue Apr 24 12:23:58 2018

@author: Nodar.Okroshiashvili
"""



class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))
        

        
 _ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)       
        
        
        