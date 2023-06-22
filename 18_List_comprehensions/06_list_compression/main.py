import random
numerous = int(input('Количество символов: '))
string_list = [random.randint(0, 2) for _ in range(numerous)]

for i in string_list:
    if i == 0:
        string_list.remove(0)
        string_list.append(0)

# print(string_list)

string_list = [i for i in string_list if i != 0]

# print(string_list)