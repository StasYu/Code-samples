word = input('Введите слово: ')

reversed_word = []
list_word = list(word)
#print(list_word)
word_lenght = len(word)

for _ in range(word_lenght):
    reversed_word.append(list_word[word_lenght - 1])
    word_lenght -= 1

#print(reversed_word)
if reversed_word == list_word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')