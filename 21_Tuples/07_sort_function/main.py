# Функция сортировки Напишите функцию, которая сортирует кортеж, состоящий
# из целых чисел по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом,
# то функция возвращает исходный кортеж.

num_tup = (2, 8, 9, 3, 1, 4, 5, 6, 7)
flag = True

for i in num_tup:
    if i != int(i):
        flag = False
if flag:
    num_list = list(num_tup)
    num_tup = tuple(sorted(num_list))

print(num_tup)




# new_nums = [i for i in num_tup]