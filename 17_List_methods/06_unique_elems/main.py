first_list = list(input('введите 3 числа без знаков и пробелов: '))
second_list = list(input('введите 7 чисел без знаков и пробелов: '))


for i_second in first_list:
    for i_count in range(second_list.count(i_second)):
        second_list.remove(i_second)

first_list.extend(second_list)
print('Новый первый список с уникальными элементами: ', first_list)



