"""
Created on Thu Mar 21 2019

@author: Nodar Okroshiashvili
"""




K = int(input())

room_numer_list = list(map(int, input().split()))

room_numer_set = set(room_numer_list)


print(((sum(room_numer_set)*K)-(sum(room_numer_list)))//(K-1))


