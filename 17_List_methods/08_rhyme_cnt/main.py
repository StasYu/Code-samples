numerous = int(input('Кол-во человек: '))
step = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', step, 'человек')

numerous_list = list(range(1, numerous + 1))
count = 0

while len(numerous_list) != 1:
    print('Текущий круг людей: ', numerous_list)
    print('Начало счёта с номера ', numerous_list[count])

    for _ in range(step):
        if count == len(numerous_list):
            count = 0
        count += 1
    count -= 1
    print('Выбывает человек под номером ', numerous_list[count])
    numerous_list.remove(numerous_list[count])
    if count >= len(numerous_list):
        count = 0

print('Остался человек под номером ', numerous_list[0])