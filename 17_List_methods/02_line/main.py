first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
temp_list = []
temp = 0

first_class.extend(second_class)

print('Первоначальный список: ', first_class)

for i in range(len(first_class)):
    temp_list.append(min(first_class))
    first_class.remove(min(first_class))

print('Отсортированный список: ', temp_list)