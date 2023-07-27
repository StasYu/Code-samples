file = open('numbers.txt', 'r')
temp_num = 0
for i_line in file:
    for i in i_line:
        if i != ' ' and i != '\n':
            temp_num += int(i)
file.seek(0)
print('Содержимое файла numbers.txt\n', file.read())
print()
file.close()
print('Содержимое файла answer.txt\n', temp_num)