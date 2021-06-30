while True:
    try:
        user_input = input('Please eneter your ID')
        if len(user_input) != 11:
            raise UserWarning
        user_input = int(user_input) # user_input = str(int(user_input)))# dvoinaja konvertacija
    except ValueError:
        print('ID code you entered is not numeric')
        continue
    except UserWarning:
        print('ID your entered is wrong')
        continue
    '''else:
        print('Your ID code is', user_input)
        break
    finally:
        print('Good bye')'''
    print(user_input, 'Your code')
    print('Good bye')
    break


if int(user_code[7:10]) in range(0:28): # Region method range
print(int(id_code[0]* 2 ) # Dlja kontrolja koda


# kod dlja proverki checkerov 388803160272