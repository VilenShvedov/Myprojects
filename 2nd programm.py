name,surname, town, birth_year = input('Please enter your name, surname, and city').split(', ')
print ("Hello" + name +  ' '  "you live in"  + town+ "you are" + str(2021 - int(birth_year)) * "old")


