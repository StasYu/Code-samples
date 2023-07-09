members_q = int(input('Сколько записей вносится в протокол? '))

if members_q < 3:
    print('введите количество записей не меньше 3-х')
else:
    score_dict = list()

    for i_member in range(members_q):
        record = input(f'{i_member + 1} запись: ').split()
        score_dict.append((int(record[0]), record[1]))

# best result code:
best_res = {}
members = {i[1] for i in score_dict}

for i_member in members:
    temp = [i_score
            for i_score, i_name in score_dict
            if i_member == i_name]
    best_res.update({i_member: max(temp)})

# winners code:
for i in range(3):
    for j in score_dict:
        if j[0] == max(best_res.values()) and j[1] in best_res.keys():
            print(f'{i + 1} место. {j[1]} ({j[0]})')
            best_res.pop(j[1])
            break