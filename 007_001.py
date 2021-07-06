'''test_list1 = [1, 2, 3, 4, 5]

for number in test_list1:
    result = number ** 2 -2
    print(result)

some_string = 'Hello people of planet earth'
for letter in some_string:
    print(letter)

some_list = ['Hello', 10, 0.23, True, None, [1, 2, 3],['one', 'two', 'three']]
for x in some_list:
    if type(x) == int or type(x) == float:
        print(x ** 2)

for num1 in range(0, 10):
    for num2 in range(0, 10):
        for num3 in range(0, 10):
            print(num1, num2, num3 )'''


'''num1 vqstavljaet 4islo 0 posel etogo num2 podstavljaet 0 i num3 toze stavit 0, 
            dalwe tolko num3 menjaet 4islo 
            tak kak mq vnutri etih ciklov(matrewka)'''
#number - eto peremenaja kotoruju mq nzavali tak , prosto ( bukva ne neset smqsla)
#cycle for ne beskone4nqi, on perebiraet vse elementq v spiske
#[1, 2, 3] eto celqi element poetomu for ego ne ispolozoval.no vse ravno po nemu prowelsja

for num in range(0, 10):
    print(num ** 2)

some_list = ['one', 'two','thr', 'Fou']
some_list = [['Jack','Smith', 25],['Mary', 'gold', 20], ['Bob', 'Dylan', 36]]
for num, num2, num3 in some_list:
    print(num, num2, num3)

print()
for person in some_list:
    num = person[0]
    num2 = person[1]
    num3 = person[2]

some_dict = {1:'One', 2:'Two', 3:'Three'}
for key, value in some_dict.items():
    print(key, value)