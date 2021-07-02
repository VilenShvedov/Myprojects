'''def first():
    number = input('Please enter number')
    return second(int(number))

def second(num):
    num = num ** 2
    print(num)
    return third(num)

def third(num):
    num = num ** 3
    print(num)
    return second(num)

first()'''

def first(number):
    result = number
    print(result)
    return first(result)

print(first(10))
x = 10
print(first(x))
