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
elif user_choice == '2':
    check_code = ((int(user_code[0] * 1) + int(user_code[1] * 2) + int(user_code[2] * 3) + int(user_code[3] * 4) + int(user_code[4] * 5) + int(user_code[5] * 6) + int(user_code[6] * 7) + int(user_code[7] * 8) + int(user_code[8] * 9) + int(user_code[9] * 1)) /10 )
    print(check_code)
    if int(user_code[7:10]) in range(0, 11):
        print('Kuressaare haigla')
    elif int(user_code[7:10]) in range(11, 20):
        print('Tartu Ülikooli Naistekliinik')
    elif int(user_code[7:10]) in range(21, 151):
        print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
    elif int(user_code[7:10]) in range(151, 161):
        print('Keila haigla')
    elif int(user_code[7:10]) in range(161, 221):
        print('Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
    elif int(user_code[7:10]) in range(221,271):
        print('Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
    elif int(user_code[7:10]) in range(271,371):
        print('Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
    elif int(user_code[7:10]) in range(371, 421):
        print("Narva haigla")
    elif int(user_code[7:10]) in  range(421, 471):
        print('Parnu haigla)' )
    elif int(user_code[7:10]) in range(471, 491):
        print('Haapsalu haigla')
    elif int(user_code[7:10]) in range(491, 521):
        print('Järvamaa haigla (Paide)')
    elif int(user_code[7:10]) in range(521, 571):
        print('Rakvere haigla, Tapa haigla')
    elif int(user_code[7:10]) in range(571, 601):
        print('Valga haigla')
    elif int(user_code[7:10]) in range(601, 651):
        print('Viljandi haigla')
    elif int(user_code[7:10]) in range(651, 701):
        print('Lõuna-Eesti haigla (Võru), Põlva haigla')
    elif int(user_code[7:10]) in range(701, 1000):
        print('Place of birth unknow')

#elif user_choice == '3':
    #pass
#first_check_code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]


#second_check_code = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
#regions = user_code [
#if int(user_code[7:10]) > 0 and int(user_code[7:10])  <= 27:  #


#user_code.index('user_code', 0, 12)
#print(user_code)
