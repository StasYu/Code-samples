first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))

def integer (number):
    number //= 1
    count_num = (- 1)
    temp = number
    while temp != 0:
        temp //=10
        count_num += 1

    reverse_num = 0
    count = 10 ** count_num
    while number != 0:
       reverse_num += (number % 10) * count
       number //= 10
       count //= 10
    return(reverse_num)


def decim (number):
    number %= 1
    while round(number,2) % 1 != 0:
        number *= 10
    count_num = -1
    temp = number
    while temp != 0:
        temp //= 10
        count_num += 1
    reverse_num = 0
    count = 10 ** count_num
    while number != 0:
        reverse_num += (number % 10) * count
        number //= 10
        count //= 10
    temp = reverse_num
    while (temp // 1) != 0:
        temp /= 10
    return(round(temp, count_num + 1))



first_int = integer(first_num)
first_dec = decim(first_num)

second_int = integer(second_num)
second_dec = decim(second_num)

print('Первое число наоборот: ', first_int + first_dec)
print('Второе число наоборот: ', second_int + second_dec)
print('Сумма:', (first_int + first_dec) + (second_int + second_dec))
