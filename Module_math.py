'''#Modul math
# vse moduli importirujutsja (import), files ne dolznq nazqvatsa modulem'''
import math

'''print(math.sqrt(25))

print(math.ceil(25.523))
print(math.floor(25.523))
print(math.sin(90))'''
'''corner = 90
corner = math.radians(90)
print(corner)
print(math.sin(corner))
corner2 = 1.5707963267948966
print(math.degrees(corner2))
print(math.sin(corner2))'''
'''print(math.pi)
print(type(math.pi))
print(math.sqrt(25))
print(250 * math.pi)'''

x, y = input('Write 2 ktates').split(' ')
x = int(x)
y = int(y)
print(math.hypot(x,y))
print(math.copysign(23, -43))