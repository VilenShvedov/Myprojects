x = 5
student = {'name': 'John','age': 32, 'courses': ['Math', 'Art', 'Programming'],
1: 'Int key', 0.2: 'float key', x: 'variable', 'var key': x}

#print(student.get('phone','Not found'))
# method get izbavljaet ot owibki esli v spiske net nuznogo zna4enija
#user_input = input('Please enter key')
#print(student.get('phone', ' Not found'))

'''if student.get(user_input, 'Not found') == 'Not found':
    student[user_input] = input(f'Please enter')

print(student[user_input])
print(student)'''


new_dict = {'surname': 'Smith', 'phone':'555-555-555'}
student.update(new_dict)
print(student)

del student['name']
print(student)

removed_item = student.pop('age')
print(removed_item)
print(student)