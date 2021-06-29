'''user_number = input('Enter some number please from 1 to 100')


if int(user_number) % (3 or 5) == 0:
    print(str(user_number) + ' FizzBuzz')
elif int(user_number) % (3 or 5) == 1:
    print(str(user_number))
elif pint(user_number) % 3 == 0:
        print(str(user_number + ' Is a fizz'))

if int(user_number) % 5 == 0:
    print(str(user_number) + ' Is a buzz')'''

for num in range(0, 100):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)