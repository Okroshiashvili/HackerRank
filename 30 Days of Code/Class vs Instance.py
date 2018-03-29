"""
Created on Mon Mar 19 11:41:13 2018

@author: Nodar.Okroshiashvili
"""

class Person:
    def __init__(self,initialAge):
        if initialAge < 0 :
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age = self.age +1
        
        
# Let check our class
        
        
# If t is set to for example 3 our class requires to enter three age to perform predefined tasks
t = int(input())

for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0,3):
        p.yearPasses()
    p.amIOld()
    print("")

