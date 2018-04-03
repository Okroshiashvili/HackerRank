"""
Created on Tue Apr  3 14:53:52 2018

@author: Nodar.Okroshiashvili
"""



N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))


# Use this iff list has unique elements
rank_x = [sorted(X).index(v)+1 for v in X]
rank_y = [sorted(Y).index(v)+1 for v in Y]

d_squared = sum([(rank_x[i] - rank_y[i])**2 for i in range(N)])



corr_coeff = 1 - (6 * d_squared) / (N*(N**2 - 1))

print(round(corr_coeff,3))



#%%

# Second Solution

"""
We know that Spearman's Rank Correlation Coefficient equals to
Pearson's Correlation Coefficient for Rank lists.

Here, I take rank lists of initial lists and calculate Pearson's 
Correlation Coefficient for them.

"""

N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))


# Use this iff list has unique elements
rank_x = [sorted(X).index(v)+1 for v in X]
rank_y = [sorted(Y).index(v)+1 for v in Y]




mu_x = sum(rank_x) / N
mu_y = sum(rank_y) / N

stdv_x = (sum([(i - mu_x)**2 for i in rank_x]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in rank_y]) / N)**0.5


# covariance = sum([(i - mu_x) * (j -mu_y) for i,j in zip(X,Y)])
covariance = sum([(rank_x[i] - mu_x) * (rank_y[i] - mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))

