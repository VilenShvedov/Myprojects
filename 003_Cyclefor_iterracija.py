#Iteracija eto perebor elementov
courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']

#for course in courses:
    #print(course)



#for number in range(1, 100):
  #print(number ** 2)

'''for num1 in range(0, 10):
    for num2 in range (0,10):
        for num3 in range(0, 10):
            for num4 in range(0, 10):
                print(num1, num2, num3, num4)'''
'''
for num in range(0, 100):
    if num % 2 == 0:
        print(num, 'Is even')
    else:
        print(num, 'Is odd')
    if num % 10 == 0:
            print(num, 'can be divided by 10')

print(num)'''

test_string = 'Hello, my name is Vilen. Everything is ok?'
test_string = test_string.split()
for word in test_string:
        print(word, len(word))
