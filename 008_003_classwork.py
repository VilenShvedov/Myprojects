import datetime
import time
tdelta = datetime.timedelta(days=7, hours=5, minutes=40 , seconds=10)
today = datetime.datetime.today()
print(today + tdelta)
date1 = today + tdelta
print()
date2 = today + tdelta

print(date1 == date2 )
