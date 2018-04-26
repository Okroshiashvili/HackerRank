"""
Created on Thu Apr 26 10:16:54 2018

@author: Nodar.Okroshiashvili
"""




def print_formatted(number):
    for i in range(1,n + 1):
        print(i,oct(i)[2:],hex(i)[2:].upper(),bin(i)[2:], sep = ' ')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#%%
        
 
def print_formatted(number):
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
