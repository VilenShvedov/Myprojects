import datetime

dt_str = 'November 30, 2020, 15:45'
dt_str1 = '12:28:33 Nov 30, 2020'
dt_str2 = 'Wed, 07/07/21'

dt_to_p = datetime.datetime.strptime(dt_str, '%B %d, %Y, %H:%M')
print(dt_to_p)
dt_to_p2 = datetime.datetime.strptime(dt_str1, '%H:%M:%S %b %d, %Y')
dt_to_p3 = datetime.datetime.strptime(dt_str2, '%a, %d/%m/%y')
print(dt_to_p2)
print(dt_to_p3)
