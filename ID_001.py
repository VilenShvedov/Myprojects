user_code = input('Enter your ID')
user_choice = input('Please choose \n'
                  '1. ID data\n'
                  '2. Validate\n'
                  '3. Exit')
if user_choice == '1':
    if int(user_code[0]) % 2 == 0:
        gender = 'Female'
    else:
        gender = 'Male'
    if user_code[0] == '1' or user_code[0] == '2':
        birth_cent = '18'
    elif user_code[0] == '3' or user_code[0] == '4':
            birth_cent = '19'
    print(user_code[5:7] + '.' + user_code[3:5] + '.' + birth_cent + user_code[1:3])
    print(gender)
elif user_choice =='2':
    pass
elif user_choice == '3':
    pass
