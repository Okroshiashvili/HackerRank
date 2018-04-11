"""
Created on Tue Apr 10 12:54:17 2018

@author: Nodar.Okroshiashvili
"""




n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    
query_name = input()

query_scores = student_marks[query_name]

print("{0:.2f}".format(sum(query_scores)/3))

