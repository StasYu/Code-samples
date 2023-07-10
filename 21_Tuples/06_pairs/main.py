original =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_line = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

updated_list = [(i, original[original.index(i + 1)]) for i in original[::2]]
print(updated_list)

#second var
#
# updated_list = []
# for i in original:
#     if i % 2 != 0:
#         updated_list.append((original.index(i) - 1, i))
#
# print(updated_list)