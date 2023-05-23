number = int(input('введите число: '))
def scd(number):
    for row in range(2, number + 1):
        if number % row == 0:
            print('Наименьший делитель, отличный от единицы:', row)
            break

scd_num = scd(number)