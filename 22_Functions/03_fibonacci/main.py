num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
init_num = [1, 1]


# solve V2
# def new_init(count, fibo=init_num):
#     new_num = sum(fibo[count-2:])
#     fibo.append(new_num)
#
#
# fibo_num = [new_init(i) for i in range(num_pos) if i >= 2]
#
# print(f'\nЧисло: {init_num[len(init_num) - 1]}')


def new_init(count, fibo, num_p=num_pos):
    count += 1
    summary = sum(fibo)
    fibo.pop(0)
    fibo.append(summary)
    if count != num_p - 1:
        new_init(count, fibo)
    return fibo


new_init(1, init_num)

print(f'\nЧисло: {init_num[1]}')