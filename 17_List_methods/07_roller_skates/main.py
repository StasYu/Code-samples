rollers_list = []
customer_list = []
temp = []
count = 0

rollers = int(input('\nКол-во коньков: '))

for i_rollers in range(rollers):
    print('Размер', i_rollers + 1, 'пары: ', end = ' ')
    size_rollers = int(input())
    rollers_list.append(size_rollers)


customer = int(input('\nКол-во людей: '))
print()

for i_customer in range(customer):
    print('Размер ноги', i_customer + 1, 'человека: ', end = ' ')
    size_customer = int(input())
    for i_rolst in rollers_list:
        if size_customer == i_rolst:
            rollers_list.remove(i_rolst)
            count += 1
        elif size_customer < i_rolst:
            rollers_list.remove(i_rolst)
            count += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)




