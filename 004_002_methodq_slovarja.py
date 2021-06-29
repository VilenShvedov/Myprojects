x = 5
student = {'name': 'John','age': 32, 'courses': ['Math', 'Art', 'Programming'],
1: 'Int key', 0.2: 'float key', x: 'variable', 'var key': x}


print(student.values())
print(student.items()) # vqvodi parq klju4-zna4enie
print(student.keys())
for key, value in student.items():
    print(key, value)

for item in student.items():
    print(item)
    print(item[0], item[1])