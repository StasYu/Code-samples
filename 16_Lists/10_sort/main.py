first_list = [1, 4, -3, 0, 10]
temp = first_list[0]
count = -1

print('Изначальный список: ', first_list)

for i_first in range(len(first_list)):
    for i_sec in range(len(first_list)):
        if first_list[i_first] < first_list[i_sec]:
            first_list[i_first], first_list[i_sec] = first_list[i_sec], first_list[i_first]

print('Отсортированный список: ',first_list)