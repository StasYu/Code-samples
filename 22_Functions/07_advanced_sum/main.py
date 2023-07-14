# Примеры вызовов функции:
#
# sum_def([[1, 2, [3]], [1], 3])
# Ответ: 10
#
# sum_def(1, 2, 3, 4, 5)
# Ответ: 15

def sum_def(*arghs, temp=[0]):
    for i in arghs:
        if isinstance(i, int):
            temp[0] = temp[0] + i
        elif isinstance(i, list):
            sum_def(*i)

    return(temp[0])


print(sum_def([[1, 2, [3]], [1], 3]))
# print(sum_def(1, 2, 3, 4, 5))