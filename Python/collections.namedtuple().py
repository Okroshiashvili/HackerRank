"""
Created on Wed Nov  7 09:56:37 2018

@author: nokroshiashvili
"""

from collections import namedtuple

N = int(input())  # Number of Students

Names = namedtuple('Students',input().split()) # namedtuple of column names


#    *input unpacks arguments and then puts in namedtuple, not vice versa
data = [Names(*input().split()) for i in range(N)]  # Contains students data

avg = sum(int(j.MARKS) for j in data) / N  # inside sum() this loop prints students marks
# This is equivalent of the following
summa = []
for j in data:
    summa.append(j.MARKS)
# We can put inside this loop sum and average as well


print('{:.2f}'.format(avg))






###############################################################################\


# Shorter Solution


from collections import namedtuple

N, Names = int(input()), namedtuple("Student", input())

print("{:.2f}".format(sum([int(Names(*input().split()).MARKS) for i in range(N)])/N))


