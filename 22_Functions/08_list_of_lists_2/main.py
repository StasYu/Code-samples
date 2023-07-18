nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
def list_opener(new_list, *args):
    for i in args:
        if isinstance(i, int):
            new_list.append(i)
        else:
            for j in i:
                list_opener(new_list, j)

    return(new_list)

new_list = []
print(list_opener(new_list, nice_list))