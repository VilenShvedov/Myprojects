#some_string = 'Vilen that\my name' # \n - perenos stroki
#print(some_string)




id_code = input("Please ennter ID: ")
if id_code.isdigit():
    print("all  digits")
if len(id_code) == 11 or len(id_code) > 10:
    if id_code[0] != "3" and id_code[0] != "4":
        print(id_code)[0]
    print("Your id is wrong")
else:
    print("your ID code is: " + id_code)
elif len(id_code) > 10:
    print("Your ID is too long")
else:
    print("Your id is too short")

