'''user_range = input('Please write numbers')
user_range2 = input('please write number')
x = int(user_range)
y = int(user_range2)'''
def fizzbuzzz(star_num, stop_num):

#if x >= y:
# print('1st number must be lower than second')
    for num in range(x, y):


        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FizzBuzz')
        elif num % 5 == 0:
            print(num, 'Buzz')
        elif num % 3 == 0:
            print(num, 'Fizz')

#1 variant zapisi
x = int(input('Please enter start number. '))
y = int(input('Please enter stop number. '))
fizzbuzzz(x, y)
#2 variant zapisi
fizzbuzzz(int(input('Please enter start number. ')), int(input('Please enter stop number. ')))