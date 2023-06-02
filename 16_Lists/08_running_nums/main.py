first_list = []
second_list = []
change = int(input('Сдвиг: '))

for _ in range (5):
    number = int(input('введите число: '))
    first_list.append(number)

print('Изначальный список: ', first_list)
list_count = (-1)

for i in range(len(first_list)):
    second_list.append(first_list[list_count])
    #print(second_list)
    list_count += 1
print('Сдвинутый список: ', second_list)
