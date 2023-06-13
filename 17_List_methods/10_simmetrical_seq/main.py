num_amount = int(input('Кол-во чисел: '))
number_list = []
new_nums = []
answer = []

def palendrom(num_list):
    reverse_list = []
    for i in range(len(num_list) - 1, -1, -1):
        reverse_list.append(num_list[i])
    if reverse_list == num_list:
        return True
    else:
        return False

for _ in range(num_amount):
    number = int(input('Число: '))
    number_list.append(number)


for i_num in range(num_amount):
    for j_num in range(i_num, num_amount):
        new_nums.append(number_list[j_num])
    if palendrom(new_nums):
        for i in range(0, i_num):
            answer.append(number_list[i])
        answer.reverse()
        break
    new_nums = []

print('Последовательность: ', number_list)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа: ', answer)
