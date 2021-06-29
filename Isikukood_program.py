while True:
    try:
        user_input = input('Please eneter your ID')
        if len(user_input) != 11:
            raise UserWarning
        user_input = int(user_input)
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


