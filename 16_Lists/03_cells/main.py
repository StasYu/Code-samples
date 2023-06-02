cell_number = int(input('Кол-во клеток: '))
efficiency_list = []

for i in range(cell_number):
    print('Эффективность', i + 1, 'клетки: ', end= '')
    cell_efficiency = int(input())
    if cell_efficiency < (i + 1):
        efficiency_list.append(cell_efficiency)

print('Неподходящие значения: ', efficiency_list)