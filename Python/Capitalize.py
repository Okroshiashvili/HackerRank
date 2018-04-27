"""
Created on Fri Apr 27 17:34:46 2018

@author: Nodar.Okroshiashvili
"""




def capitalize(string):
    return ' '.join(i[:1].upper() + i[1:] for i in string.split(' ')) 



if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)

