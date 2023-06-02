word = input('Введите слово: ')
words_list = list(word)
trash_list = []
count = 0
unique_count = 0

for i in words_list:
    for i_trash in words_list:
        if i == i_trash:
            count += 1
    if count < 2:
        unique_count += 1
    count = 0

print('Кол-во уникальных букв: ', unique_count)