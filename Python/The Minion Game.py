"""
Created on Mon May 14 13:12:55 2018

@author: Nodar.Okroshiashvili
"""



def minion_game(string):
    vowels = 'AEIOU'
    length = len(string)
    Kevin = sum([length - i for i in range(length) if string[i] in vowels])
    Stuart = sum([length - i for i in range(length) if string[i] not in vowels])
    if Stuart > Kevin:
        print("Stuart" + " " + str(Stuart))
    elif Stuart < Kevin:
        print("Kevin" + " " + str(Kevin))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
