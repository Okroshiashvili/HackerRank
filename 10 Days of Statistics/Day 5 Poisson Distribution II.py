"""
Created on Wed Mar 28 14:21:19 2018

@author: Nodar.Okroshiashvili
"""

mean_X, mean_Y = [float(num) for num in input().split(" ")]


cost_A = 160 + 40 * (mean_X + mean_X**2)

cost_B = 128 + 40 * (mean_Y + mean_Y**2)

print(round(cost_A,3))
print(round(cost_B,3))
