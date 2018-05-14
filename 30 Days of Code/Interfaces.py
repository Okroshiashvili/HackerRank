"""
Created on Mon May 14 12:43:27 2018

@author: Nodar.Okroshiashvili
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
        
        
        
        
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        x = []
        for i in range(1, n+1):
            
            if n % i == 0:
                x.append(i)
            else:
                pass
        return sum(x)
    
    
    
n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

