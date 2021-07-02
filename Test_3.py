a, b, c = input('Please enter triangle sides A B C').split(',')
a, b, c = float(a), float(b), float(c)
check = (((a ** 2 ) + (b ** 2 )) - (c ** 2 ))
check = float(check)
if float(check) == 0 :
    print('Triangle is a rectangular')
else:
    print('Triangle is not rectangular')
