import datetime #as dt #  AS pereimenovqvaet biblioteku

today = datetime.date.today()
print(today)
print(type(today))
year, month, day = input('Print date: ').split('.')
user_date = datetime.date((int(year)), int(month), int(day))
print(user_date.year)
print(type(user.date.year))
print(user_date.month)
print(type(user.date.month))
print(user_date.day)
print(type(user.date.day))
print(today.year - user_date.year)

'''today = datetime.date.today()
some_date = datetime.date(1990, 10, 7)
print(some_date.weekday())
print(some_date.isoweekday())'''

'''datetime.weekday() - день недели в виде числа, понедельник - 0, воскресенье - 6.

datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.'''
'''print(datetime.date.today())
print(datetime.datetime.now())'''

'''tdelta = datetime.timedelta(days=7)
today = datetime.date.today()

print(today - tdelta)
till_bd = datetime.date(2022, 3, 16)
print(till_bd - today)

bd_delta = till_bd - today
print(bd_delta)
print(till_bd)
print(today)'''
#Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.

today = datetime.datetime.now()
bday = datetime.datetime(2022, 3 ,16, 15, 30, 45) # Esli ne ukazano 4islo, minuta, 4as, sekunda po umol4aniju 0
print(bday - today)

today1 = datetime.date.today()
bday1 = datetime.date(2080, 3, 16)
delta_time = bday - today
print(delta_time)
print(delta_time.days)
print(delta_time.microseconds)
print(delta_time.seconds)
print(delta_time.total_seconds())
#print(delta_time.)

