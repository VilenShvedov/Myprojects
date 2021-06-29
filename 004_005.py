'''disstance_to_target = float(input('Please enter distance in KM: '))
step = 0.5
current_position = 0
cnt = 0

s4et4ik wagov

while current_position != disstance_to_target * 1000:
    current_position += step
    cnt += 1

print(current_position)
print(cnt)'''

# method "pass" pozvoljaet nam izbavitsja ot owibki
'''condition = True
while condition:
    user_choice = input("Please choose:\n"
                    "1: Print 'Hello'\n"
                    '2: Print "world\n'
                    '3: Exit\n'
                    '->')

    if user_choice == '1':
       print('hello')
    elif user_choice == '2':
         continue # propuskaet cqkl i na4inaet zanovo
         print('world')
    elif user_choice == '3':
         condition = False
         print("Good bye")
         break # razrqvaet cqkl
    else:
         print('Wrong choice')'''

for letter in 'Python':
    if letter == "t":
       print('Reached letter "t"')
    else:
        continue
    print('Hello')
