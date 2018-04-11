"""
Created on Tue Apr 10 11:06:42 2018

@author: Nodar.Okroshiashvili
"""


N = int(input())
marks = [[input(),float(input())] for _ in range(N)]
marks = sorted(marks)


grades = [grades[1] for grades in marks]
second_lowest = sorted(list(set(grades)))[1]

for i in marks:
    if i[1] == second_lowest:
        print(i[0])


for _ in range(int(input())):
    name = input()
    score = float(input())

