'''for num in range(1, 100):
    number = ''
    if num % 5 == 0 and num % 3 == 0:
        number = (number + 'BuzzFizz')
    if num % 5 == 0:
        number = (number + 'Fizz')
    if num % 3 == 0:
       number = (number + " Buzz")

print(number)'''


for number in range(1, 101):
    if number % 5 == 0 and number % 3 ==0:
         print(number, 'Fizz Buzz')
    elif number % 3 == 0:
        print(number, 'Fizz')
    elif number % 5 == 0:
        print(number, 'Buzz')


