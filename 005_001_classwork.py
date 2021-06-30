def print_message(name, surname, age, salary, gender):
    if gender.lower() == "male":
        result = f'His name is {name} {surname}. He is {age} years old. His salary is {salary:.2f}.'# .2f eto float
#kotorqi piwet posle zapjatoi 2 cifrq
        return print(result)
    elif gender.lower() == "female":
        result = f'Her name is {name} {surname}. SHe is {age} years old. Her salary is {salary:.2f}'
        return print(result)

employees = [['John', 'Smith', 33, 1500, 'maLe'],['Mary','Gold', 27, 2500, 'fEmale'],
            ['Jack', 'Black', 45, 2456, 'male']]

for employee in employees:
    print_message(employee[0], employee[1], employee[2], employee[3],employee[4])

for name, surname, age, salary, gender in employees:
    print_message(name, surname, age, salary, gender)
#john_var = ['John', 'Smith', 33, 1500, 'maLe']
#print_message('John', 'Smith', 33, 1500, 'maLe')
#print_message('Mary','Gold', 27, 2500, 'fEmale')
#mary_var = ['Mary','Gold', 27, 2500, 'fEmale']