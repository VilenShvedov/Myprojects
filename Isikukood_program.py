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
    else:
        print('Your ID code is', user_input)
        break
        print(int(id_code[0] * 1) + int(id_code[1] * 2)
    finally:
        print('Good bye')'''
    print(user_input, 'Your code')
    print('Good bye')
    break


'''if int(user_code[7:10]) in range(0:28): # Region method range'''
print(int(id_code[0]* 1 ) + int(id_code[1] * 2) + int(id_code[2] * 3) + int(id_code[3] * 4) + int(id_code[4] * 5) + int(id_code[5] * 6)  + int(id_code[6] * 7) +
      int(id_code[7] * 8 ) + int(id_code[8] * 9) + int(id_code[9] * 1)) /
 print(int(id_code[0] * 3) + int(id_code[1] * 4) + int(id_code[2] * 5) + int(id_code[3] * 6) + int(
        id_code[4] * 7) + int(id_code[5] * 8) + int(id_code[6] * 9) +
          int(id_code[7] * 1) + int(id_code[8] * 2) + int(id_code[9] * 3))


# kod dlja proverki checkerov 388803160272

