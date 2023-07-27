zen_file = open('zen.txt', 'a')
zen_file.write('\n')
zen_file.close()

zen_file = open('zen.txt', 'r')
new_list = list()
new_file = open('new_zen', 'a')

for i_line in zen_file:
    new_list.append(i_line)

for i_elem in new_list[::-1]:
    new_file.write(i_elem)

new_file.close()
zen_file.close()

new_file = open('new_zen', 'r')

print(new_file.read())