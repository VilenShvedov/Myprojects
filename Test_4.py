user_word = input('Please write some words').split(',')
user_word = list(user_word[::-1])

user_word.sort(reverse=True)
print(user_word)
