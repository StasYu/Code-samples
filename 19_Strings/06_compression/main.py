string = list(input('Введите строку: '))
temp_str = [[]]
temp = string[0]
count = 0

for i in string:
    if temp == i:
        temp_str[count].extend(i)
    else:
        temp = i
        count += 1
        temp_str.append([i])

final = [''.join([i[0], str(len(i))]) for i in temp_str]

print('Закодированная строка: ', end = '')
for i in final:
    print(i, end = '')
