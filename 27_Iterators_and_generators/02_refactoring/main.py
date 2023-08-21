list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

def my_gen(first: list, second: list) -> tuple[int]:

    for x in first:
        for y in second:
            result = x * y
            yield x, y, result


gen = my_gen(list_1, list_2)

for x, y, result in gen:
    print(x, y, result)
    if result == to_find:
        print('Found!!!!')
        break
