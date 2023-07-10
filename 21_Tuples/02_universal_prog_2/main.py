# example = [100, 200, 300, 'буква', 0, 2, 'а', 555, 'sffd', 2173, 'dshak', 21321, 212, 21222, 12121, 2121]
# example = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
example = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:16,17:17}
def is_prime(index):

    flag = True
    for i in range(2, index // 2 + 1):
        if index % i == 0:
            flag = False
    if index == 0:
        flag = False
    if index == 1:
        flag = True
    return (flag)

def returned(result):
    return(tuple(result))

result = [
    i_elem
    for i_index, i_elem in enumerate(example)
    if isinstance(i_elem, int | tuple | str | list | dict)
       and is_prime(i_index)
]

print(len(example))
print(f'Результат: {returned(result)}')