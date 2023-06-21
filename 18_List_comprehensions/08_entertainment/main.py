import random

stick_count = int(input('Кол-во палок: '))
throw_count = int(input('Кол-во бросков: '))
new_list = list('I' * stick_count)
# print('new list = ', new_list)
def i_left(sticks):
    left = random.randint(0, sticks - 1)
    return(left)
def i_right(sticks, i_left):
    right = random.randint(i_left + 1, sticks)
    return(right)

for i in range(throw_count):
    left = i_left(stick_count)
    right = i_right(stick_count, left)
    print('Бросок', i, 'Сбиты палки с номера ', left,
'по номер', right)
    sub_list = ['.'
                if (i >= left - 1) and (i <= right - 1)
                else 'I'
                for i in range(stick_count)
                ]
    # print('\nsublist = ', sub_list)

    new_list = ['.'
                if sub_list[i] == '.' or new_list[i] == '.'
                else 'I'
                for i in range(stick_count)
                ]
    # print('new list = ', new_list)

print('Результат: ')
for i in (new_list):
    print(i, end='')