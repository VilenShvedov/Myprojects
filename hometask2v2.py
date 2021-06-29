for num in range(1, 100):
    number = ''
    if num % 5 == 0 and num % 3 == 0:
        number = (number + 'BuzzFizz')
    if num % 5 == 0:
        number = (number + 'Fizz')
    if num % 3 == 0:
       number = (number + " Buzz")

print(number)


