number = int(input('Введите число: '))

def summary(number):
    summary = 0
    while number != 0:
        summary += number % 10
        number //= 10
    return (summary)

def number_count(number, summary):
    number_count = 0
    dif_numbers = 0

    while number != 0:
        number //= 10
        number_count += 1
    print('Количество цифр в числе:', number_count)
    print('Разность суммы и количества цифр:', dif_numbers)
    return(number_count)


print('Сумма чисел: ', summary(number))
summary_n = summary(number)
new_number_count = number_count(number, summary_n)