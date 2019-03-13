"""
Created on Wed Mar 13 09:33:04 2019

@author: Nodar Okroshiashvili
"""




n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))




print(len(english.symmetric_difference(french)))





