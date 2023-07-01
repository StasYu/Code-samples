text = input('Введите текст: ')

unique_text = set(text)
inverted_dict = dict()
text_dict = {i_sym: text.count(i_sym) for i_sym in unique_text}

print('Оригинальный словарь частот:')


for i_sym in text_dict:
    print(f'{i_sym} : {text_dict[i_sym]}')


print('\nИнвертированный словарь частот:')

for i_key in range(1, max(text_dict.values()) + 1):
    temp_list = [j_sym for j_sym in text_dict if text_dict[j_sym] == i_key]
    print(f'{i_key} : {temp_list}')
    inverted_dict.update({i_key:temp_list})

