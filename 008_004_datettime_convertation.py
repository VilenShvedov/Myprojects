import datetime

'''dt_str = 'November 30, 2020'
dt_str1 = 'Nov 30, 2020'
dt_str2 = 'Wed. 07/07/2021'
dt_str3 = '7 June 2021, 12:56'
today = datetime.datetime.today()
print(today.strftime('%c'))
str_to_date = datetime.datetime.strptime(dt_str, '%B %d, %Y')
str_to_date3 = datetime.datetime.strptime(dt_str3, '%d %B %Y, %H:%M')'''
dt_str3 = '7 Июнь 2021, 12:56'
dt_str3 = dt_str3.replace('Июнь', 'June')
str_to_date3 = datetime.datetime.strptime(dt_str3, '%d %B %Y, %H:%M')
print = datetime.datetime.today()
print(today - str_to_date3)