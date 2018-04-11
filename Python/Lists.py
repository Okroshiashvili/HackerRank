"""
Created on Tue Apr 10 13:34:33 2018

@author: Nodar.Okroshiashvili
"""


N = int(input())

listi = []
for n in range(N):
    x = input().split(' ')
    command = x[0]
    if command == 'insert':
        listi.insert(int(x[1]),int(x[2]))
    elif command == 'print':
        print(listi)
    elif command == 'remove':
        listi.remove(int(x[1]))
    elif command == 'append':
        listi.append(int(x[1]))
    elif command == 'sort':
        listi.sort()
    elif command == 'pop':
        listi.pop()
    elif command == 'reverse':
        listi.reverse()
    else:
        pass
    