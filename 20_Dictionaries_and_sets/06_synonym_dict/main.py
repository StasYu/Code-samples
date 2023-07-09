q_words = int(input('Введите количество пар слов: '))
pair_dict = dict()
flag = False

for i in range(q_words):
    pair = input(f'{i + 1} пара: ').split(' - ')
    pair_dict.update({pair[0]:set(pair)})


while True:
    word = input('\nВведите слово: ').title()
    for i in pair_dict.values():
        if word in i:
            print('Синоним:', *(i - set({word})))
            flag = True
    if not flag:
        print('Такого слова в словаре нет.')
    flag = False