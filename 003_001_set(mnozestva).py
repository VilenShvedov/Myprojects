courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
courses2 = {'Math', 'History'}
numbers = [1, 2, 3, 4, 5, 6, 6, 6, 6,]
'''empty_set = set()
print(type(empty_set))
empty_list = list
print(type(empty_list))
empty_tuple = tuple()
print(type(empty_tuple))'''
''''#pri vqvode seta on ne vqvodit duplikatq

print(courses.intersection(courses2)) # intersection - sovpadenie
print(courses.intersection(courses))

print(courses.difference(courses2)) # sovpadenija
print(courses2.difference(courses))

print(courses.union(courses2)) # objedinjaet setq - eto razovoe deistvie
print(courses)'''

print(courses.issuperset(courses2)) # sravnivaet odinakovqe elementq, javljaetsa li supersetom
print(courses2.issubset(courses))

#issuperset proverjaet esli v bolwom sete malenkij set, issubset obratnoe deistvie

