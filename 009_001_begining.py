with open('trimushketera.txt', 'r', encoding='utf8') as file:
    data = file.read().lower()
    symbols = ['.', ',', '!', '?', ':', '-']
    for sym in symbols:
        data = data.replace(sym,'')
        print(data)
    '''word_list = data.split()
     with open('trimushketera.txt', 'w',encoding='UTF8') as wfile:
        wfile.write(f'There are {len{word_list}} word in text. \n'
                f'There are {len(set(word_list))} unique words in text ')'''
    print(len(word_list))
    print(len(set(word_list)))

"Как искать слова в текстовых файлах"
