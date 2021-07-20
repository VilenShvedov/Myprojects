import datetime
import time

#year, month, day = input('Print date: ').split('.')
today = datetime.date.today()
bday = datetime.date(1994, 9, 10)

days_2 = (today - bday)

print(days_2[0])

#print('You are ' + (days_2.date) + ' ' +'years old ')
print(today.year)
print(today.month)
print(today.day)
print(type(days_2))