test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 8, 8, 2, 3, 2, 3, 4,]
empty_dict = {}
for num in test_list1:
    empty_dict[num] = test_list1.count(num)
print(empty_dict)

empty_list = []
for x in empty_dict.keys():
    if empty_dict[x] == max(empty_dict.values()):
        empty_list.append(x)

print(empty_list)

'''max_count = 0
new_list = []

for num in test_list1:
    if test_list1.count(num) > max_count:
        max_count = test_list1.count(num)



for num in test_list1:
    if test_list1.count(num) == max_count:
        new_list.append(num)

print(new_list)
new_list = list(set(new_list))
print(new_list)
print(max_count)'''