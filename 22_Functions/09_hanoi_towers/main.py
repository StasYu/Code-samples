
# Введите количество дисков: 2
# Переложить диск 1 со стержня номер 1 на стержень номер 2

numbers = int(input('Введите количество дисков: '))
first = 1
second = 2
third = 3

# def moving(number, first, second, third):

def moving(number, first, second):
    for i in range(1, number):
        print(f'Переложить диск {i} со стержня номер {first} на стержень номер {second}')
    return


if numbers == 1:
    print('Переложить диск 1 со стержня номер 1 на стержень номер 3')
else:
    moving(numbers, first, second)
    print(f'Переложить диск {numbers} со стержня номер 1 на стержень номер 3')
    moving(numbers, second, third)
