friends_amount = int(input('Кол-во друзей: '))
checks_amount = int(input('Долговых расписок: '))

balance_list = []
check_list = []
total_list = []
temp = 0

for _ in range(checks_amount):
    check_list.append(int(input('Кому: ')))
    check_list.append(int(input('От кого: ')))
    check_list.append(int(input('Сколько: ')))
    balance_list.append(check_list)
    check_list = []

for i_friends in range(friends_amount):
    for i in balance_list:
        if i_friends + 1 == i[0]:
            temp -= i[2]
        elif i_friends + 1 == i[1]:
            temp += i[2]
    total_list.append(temp)
    temp = 0

print('Баланс друзей:')
for i_num in range(friends_amount):
    print(i_num + 1, ':', total_list[i_num])
