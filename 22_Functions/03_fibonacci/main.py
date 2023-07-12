num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
init_num = [1, 1]

def new_init(count, fibo=init_num):
    new_num = sum(fibo[count-2:])
    fibo.append(new_num)


fibo_num = [new_init(i) for i in range(num_pos) if i >= 2]

print(f'\nЧисло: {init_num[len(init_num) - 1]}')