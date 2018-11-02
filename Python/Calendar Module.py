"""
Created on Fri Nov  2 09:44:58 2018

@author: nokroshiashvili
"""



import calendar

MM, DD, YYYY = map(int,input().split(' '))

print(calendar.day_name[calendar.weekday(int(YYYY),int(MM),int(DD))].upper())

