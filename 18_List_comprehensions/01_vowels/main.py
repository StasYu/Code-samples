adjective = ['а', 'и', 'е', 'ё', 'о', 'у', "ы", 'э', 'ю', 'я']
text = list(input('Введите текст: '))

adj_list = [i_let for i_let in adjective for i_sym in text if i_let == i_sym]
print('Список гласных букв: ', adj_list)
print('Длина списка: ', len(adj_list))