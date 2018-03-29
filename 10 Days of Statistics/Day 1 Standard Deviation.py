"""
Created on Mon Mar 26 13:29:51 2018

@author: Nodar.Okroshiashvili
"""

N = int(input().strip())
X = list(map(int, input().strip().split(' ')))


mean = sum(X) / N

variance =sum([(i - mean)**2 for i in X]) / N

standard_deviation = round(variance ** 0.5, 1)

print(standard_deviation)


