courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']
courses2 = ['Art', 'English']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 1, 1]
# Operator sravnenie ne mozet sortirovat spisok so slovami i bukvami
#numbers.sort(reverse=True) # Sortirovka v obratnom proajdke
#courses.sort()

#print(courses)
#print(sorted(courses, reverse=True))
#print(courses, end='******') # method END vstavljaet simvolq v konec stroki no ne perenosit v novuju stroku

'''print(min(numbers))# minimalnoe 4islo
print(min(courses))

print(max(numbers))
print(max(courses))

print(sum(numbers)) # method sum skladqvaet 4isla
print(numbers.count(1)) # s4itaet skolko raz v spiske vstre4aetsa element i vqvodit v integer
check_number = 3
#print(numbers.count(check_number))
#print(courses.index('Math', 2, 5))  # Method index nahodit index kakogoto elementa ( iwet index,s kakogo elemnta, po kakoi element]
math_index = courses.index('Math')
print(courses[math_index])'''

#print('Math' in courses)
#if 'Math' in courses:                  izu4it method
    #print(courses.index('Math'))
#else:
    #print('There is no English in list')

#some_string = 'Hello world, how are you?'
#print(some_string.split(', '))
#method split v skobkah ukazavetsa po kakomu priznaku delista stroka
#some_string.replace('?', 'asdasdasd')
#print(some_string)

#print('***** '.join(courses))
# method .join mozet obratno soedinit spisok v stroku
#print(type(', '.join(courses)))
#new_string = '*****'.join(courses)
#print(new_string)
new_courses = courses.copy() # sozdaet kopiju peremenoi pri etom original ostaetsa neizmenqm
new_courses[4] = 'Art'
courses[1] = 'English' # pridaet English v stroke 2 mesto
print(new_courses)
print(courses)



