"""
Created on Tue Apr  3 13:53:40 2018

@author: Nodar.Okroshiashvili
"""


N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

stdv_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5


# covariance = sum([(i - mu_x) * (j -mu_y) for i,j in zip(X,Y)])
covariance = sum([(X[i] - mu_x) * (Y[i] - mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))



