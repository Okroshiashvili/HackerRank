"""
Created on Thu Mar 15 10:56:40 2018

@author: Nodar.Okroshiashvili
"""



meal_cost = float(input().strip())
tip_percent = int(input().strip())
tax_percent = int(input().strip())

tip = meal_cost * (tip_percent/100)
tax = meal_cost * (tax_percent/100)   

total_cost = round(meal_cost + tip + tax)
  
print("The total meal cost is" +" " + str(total_cost) + " " + "dollars.")

