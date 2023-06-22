nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [
    i_num for i_list in range(len(nice_list))
    for i_sym in range(len(nice_list[i_list]))
    for i_num in nice_list[i_list][i_sym]
]

print(new_list)
