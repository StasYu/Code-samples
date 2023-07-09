first_str = list(input('Первая строка: '))
second_str = list(input('Вторая строка: '))
flag = True
# print('str = ', str(first_str))

for i in range(len(first_str) + 1):
    temp = [first_str[0]]
    if str(first_str).startswith(str(second_str)):
        print('Первая строка получается из второй со сдвигом', i)
        flag = False
        break
    else:
        first_str.extend(temp)
        first_str.remove(first_str[0])

if flag != False:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')