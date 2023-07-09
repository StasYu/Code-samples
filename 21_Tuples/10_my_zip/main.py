string = input('Строка: ')
num_tuples = input('Кортеж чисел: ')

# string = 'abcd'
# num_tuples = (10, 20, 30, 40)

zipped_string = zip(string, num_tuples)

print('Результат:')
print(zipped_string)
for i in zipped_string:
    print(i)