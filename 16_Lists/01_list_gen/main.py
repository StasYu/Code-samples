n_num = int(input('Enter N number: '))
n_list = []
for i in range(1, n_num + 1):
    if i // 2 != i / 2:
        n_list.append(i)

print(n_list)
