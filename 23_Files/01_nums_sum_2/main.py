file = open('numbers.txt', 'r')
temp_num = 0
for i_line in file:
    temp = i_line.split()
    if len(temp) > 0:
        temp_num += int(temp[0])

file.seek(0)
print('Содержимое файла numbers.txt\n', file.read())
print()
file.close()
print('Содержимое файла answer.txt\n', temp_num)