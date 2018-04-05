"""
Created on Wed Apr  4 13:29:12 2018

@author: Nodar.Okroshiashvili
"""


import numpy as np

m,n = [int(i) for i in input().strip().split(' ')]

X = []
Y = []

for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])
    

q = int(input().strip())
X_new = []
for x in range(q):
    X_new.append(input().strip().split(' '))

# Convert list into numpy array
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

# Insert constants into the array
X = np.insert(X,0,1,axis=1)
X_new = np.insert(X_new,0,1,axis=1)


# Matrix operations
XT_X = np.dot(X.transpose(),X)

XT_X_inv = np.linalg.inv(XT_X)

XT_X_inv_XT = np.dot(XT_X_inv,X.transpose())

B = np.dot(XT_X_inv_XT,Y)

# Prediction
Y_hat = np.dot(X_new,B)

# Convert array into list
Y_hat = Y_hat.tolist()

# Flatten the list of list
Y_hat = [i for j in Y_hat for i in j ]


# Print the rounded output
for i in Y_hat:
    print(round(i,2))


