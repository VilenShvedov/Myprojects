workers = [('Alex', 'Simth','21', 'male'), ('John', 'Brown', '45', 'male'),
           ('Mary', 'Gold', '30', 'female')]

for name, surname, age, gender in workers:
    if gender == 'male':
        print(f'This is ' + name + ' ' + surname + ' He is ' + age + ' years old')
    elif gender == 'female':
        print(f'This is ' + name + ' ' + surname + ' She is ' + age + ' years old')