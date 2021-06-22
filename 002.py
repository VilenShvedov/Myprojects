string_sample = "Hello world world world "
string_sample2 = "first letteR is lowErcase"
string_sample3 = "  extra whitespace string"
german_sample = "der fluÄ"
some_string = "Hello"
count = 2

print(string_sample[1:6])
print(type(string_sample[1:6]))
print(string_sample.replace("world", "planet", count))

print(string_sample).find("world", 0, 12)
print(string_sample[6:])
found_index = string_sample.find("world", 0, 12)
print(string_sample[found_index:])



#print(string_sample.count("world"))
#count_number = string_sample.count("world")
#string_slice = string_sample[0:5] #
#print(string_slice)
#print(type(string_slice))
#string_lower = string_sample.lower()
#print(string_lower)
#print(type(string_lower))





#print(string_sample2.capitalize()) # Capitalize piwet predlozenie s bolwoi bukvq, vse bukvq opuskaet a 1 podnimaet
#print(string_sample2.capitalize().lower().upper())
#print(string_sample3.strip()) # Vqrezaet probelq po krajam( vnutri teksta ne trogaet)
#print(string_sample[6:1])
#print(type(string_sample[6:1]))
#print(string_sample.replace(string_sample[6:], string_sample2[0:5] ))  # Zamenjaet 1 na 2
#print(string_sample.replace("world", "planet", count)) # 1 ukazqvaet skolko raz budet zamenjat slova









#print(string_sample[0:10]) #последняя цифра в индексации это номер буквы которая не будет отоброжена
#print(string_sample[0:10:2] # Индексация с шагом в два, пропускате каждую вторую букву или символ, пробел тоже считается
#[start:stop:step] схема индексации
#print(len(string_sample))  считает кол-во знаков в строке


#print(string_sample[0:5])
#print(len(some_string))
#print(type(len(some_string)))
#print(some_string in  "Hello world", "world" in "Hello world") #ищем совпадения в строке

#print("Hello world" .lower)
#print(string_sample.lower()) # переносит текст в нижний реестр
#print(string_sample.upper()) #переносит текст в верхний реестр
#print(german_sample.lower())
#print(german_sample.casefold()) #меняет альтернативную букву на латиницу #




