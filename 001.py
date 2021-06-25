some_list = [['name','Roman'],['surname', 'kustelepa']]

for key, value in some_list:
    print(key)
    print(value)

for element in some_list:
    for value in element:
        print(value)
