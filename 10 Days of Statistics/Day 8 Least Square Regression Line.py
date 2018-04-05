"""
Created on Wed Apr  4 09:55:41 2018

@author: Nodar.Okroshiashvili
"""

# OLS from scratch


N = int(input())

X = []
Y = []
for i in range(N):
    grades = [int(i) for i in input().split()]
    X+=[grades[0]]
    Y+=[grades[1]]

mean_x = sum(X) / N
mean_y = sum(Y) / N

def ols(X,Y):
    sumXY = sum([X[i] * Y[i] for i in range(N)])
    sum_X_squared = sum([X[i]**2 for i in range(N)])
    sumX_squared = sum(X)**2
    
    b = ((N * sumXY) - (sum(X)*sum(Y))) / ((N*sum_X_squared) - sumX_squared)
    a = mean_y - b*mean_x
    
    SST = sum([(Y[i] - mean_y)**2 for i in range(N)])
    y_hat = [a + (b*X[i]) for i in range(N)]
    residuals = [Y[i] - y_hat[i] for i in range(N)]
    SSR = sum([(y_hat[i] - mean_y)**2 for i in range(N)])
    SSE = sum([(y_hat[i] - Y[i])**2 for i in range(N)])
    R_squared = SSR / SST
    return {'Intercept':a, 'Slope':b, 'SST':SST, 'SSR':SSR, 'SSE':SSE, 'R_Squared':R_squared}

print(ols(X,Y))



#%%

# Solution




X = []
Y = []
for i in range(5):
    grades = [int(i) for i in input().split()]
    X+=[grades[0]]
    Y+=[grades[1]]

mean_x = sum(X) / 5
mean_y = sum(Y) / 5


sumXY = sum([X[i] * Y[i] for i in range(5)])
sum_X_squared = sum([X[i]**2 for i in range(5)])
sumX_squared = sum(X)**2
    
b = ((5 * sumXY) - (sum(X)*sum(Y))) / ((5 * sum_X_squared) - sumX_squared)
a = mean_y - b * mean_x

print(round(a+b*80,3))

