'''import calendar

print(calendar.month(2021, 7, w=3, l=2))
print(calendar.calendar(2021, w=2, c=7, m=3))
#print(calendar.HTMLCalendar().formatyear(2021))
print(calendar.weekday(2021, 7, 6))
print(calendar.isleap(2021))
print(calendar.leapdays(2020, 2029))'''

import time
'''start = time.time()
print('Hello')
print('World')
time.sleep(5) # - zaderzka
stop = time.time()
print(stop - start)
print(time.time())
print(time.time())
print(time.asctime())
print(time.gmtime())
print(type(time.gmtime()))
print(list(time.gmtime()))
now = time.gmtime()
print(time.gmtime()[0])
time.sleep(1)

now = time.asctime()
print(type(now))
print(now[4:10])
print(len(now))'''

now = time.localtime()
print(now)
