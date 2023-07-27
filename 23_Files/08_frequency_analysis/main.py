import string
alpha = string.ascii_letters
count = 0
# Создание файла
file = open('text.txt', 'w')
file.write('Mama myla ramu.')
file.close()
# Переработка содержимого файла в множество
file = open('text.txt', 'r')
file_dict = dict()
file.seek(0)
#создание словаря из букв и количества
for i_line in file:
    for j_let in i_line.lower():
        if j_let in alpha:
            file_dict[j_let] = i_line.lower().count(j_let)

total = [int(i) for i in file_dict.values()]
total = sum(total)

file_dict = {i : round((j/ total),3) for i, j in file_dict.items()}
sorted_dict = {i:list() for i in file_dict.values()}

#сортируем словарь по значениям и ключам
for i,j in file_dict.items():
    sorted_dict.get(j).append(i)

for i in sorted_dict.values():
    i.sort()
    print(i)

sorted_dict = dict(sorted(sorted_dict.items(), reverse=True))
print(sorted_dict)
# Запись в файл
new_file = open('analysis.txt ', 'w')
for i_key, i_val in sorted_dict.items():
    for j_val in i_val:
        new_file.write(f'{j_val} {i_key}\n')

new_file.close()