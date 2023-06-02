card_number = int(input('Кол-во видеокарт: '))
card_list_old = []
card_list_new = []

max_elem = 0

for i in range (card_number):
    print((i + 1), 'Видеокарта: ', end='')
    card_type = int(input(''))
    card_list_old.append(card_type)
    if card_type > max_elem:
        max_elem = card_type
print('Старый список видеокарт:', card_list_old)

for i in card_list_old:
    if i != max_elem:
        card_list_new.append(i)

print('Новый список видеокарт: ', card_list_new)


