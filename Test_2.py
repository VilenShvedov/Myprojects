a,b = input('Please write triangle legs').split(',')
a,b = int(a), int(b)
c = (((a * a) + (b * b)) ** 0.5)
print('Triangle hypotenuse is ' + str(c) )