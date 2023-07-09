# string = input('Строка: ')
# num_tuples = input('Кортеж чисел: ')

string = 'abcd'
num_tuples = (10, 20, 30, 40)

def minimal_len(string, num_tuples):
    return(min(len(string), len(num_tuples)))

# zipped_string = zip(string, num_tuples)
#
# print('Результат:')
# print(zipped_string)
# for i in zipped_string:
#     print(i)

pair = ((string[i], num_tuples[i]) for i in range(minimal_len(string, num_tuples)))

print(pair)
for i in pair:
    print((i[0], i[1]))