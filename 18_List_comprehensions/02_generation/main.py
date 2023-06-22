
n_list = list(range(int(input('Введите длину списка: '))))
print(n_list)


result_list = [1 if i_num % 2 == 0  else n_list[i_num] % 5 for i_num in n_list]
print(result_list)