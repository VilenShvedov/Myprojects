courses = ('History', 'Math', 'Literature', 'Physics', 'Programming', 'Math')
courses2 = ('Art', 'English')
empty_tuple = ()
print(type(empty_tuple))
courses = list(courses) # konvertiruem v spisok ( spisok izmenjaemqm)
courses.pop()
courses = tuple(courses)
print(courses)
some_string = 'Hello world'
print(list(some_string))
courses3 = list(courses)
print(courses3)
print(courses)


# Kortezh (tuple) javljaetsa neizmenjaemqm methodom
