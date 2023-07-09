q_orders = int(input('Введите кол-во заказов: '))
dict_orders = dict()


for i_count in range(q_orders):
    name = input(f'{i_count + 1} заказ: ').split()
    name[2] = int(name[2])
    if name[0] not in dict_orders:
        dict_orders[name[0]] = {name[1]: [name[2]]}
    else:
        if name[1] not in dict_orders.get(name[0], []):
            dict_orders[name[0]][name[1]] = [name[2]]
        else:
            temp = dict_orders[name[0]].get(name[1])
            temp.extend([name[2]])
            dict_orders[name[0]][name[1]] = temp

for i in dict_orders:
    print(f'{i}: ')
    for j in dict_orders[i]:
        print(f'        {j}: {sum(dict_orders[i][j])}')