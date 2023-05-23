first_year = int(input('Введите первый год: '))
second_year = int(input('Введите второй год: '))

print ('Года от', first_year, 'до', second_year, 'с тремя одинаковыми цифрами:')


for difference in range(first_year, second_year + 1):
    temp_dif = difference
    equal_first = temp_dif % 10
    #print(equal_first, 'first')
    equal_second = (temp_dif // 10) % 10
    #print(equal_second, 'second')
    difference //= 100
    #print(difference, ' current dif')
    while difference != 0:
        equal_temp = difference % 10
        if (equal_first == equal_temp) and (equal_second == equal_temp):
            print(temp_dif)
            break
        elif equal_first == equal_temp:
            equal_second = equal_first
        elif equal_second == equal_temp:
            equal_first = equal_second
        difference //= 10



