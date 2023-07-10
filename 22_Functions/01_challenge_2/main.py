def list_of_nums(num, new_num = 0):
    new_num += 1
    print(new_num)
    if new_num != num:
        list_of_nums(num,new_num)


num_q = int(input('enter number q-ty: '))
result = list_of_nums(num_q)
