team_list = ['Артемий', 'Борис', 'Влад', 'Гоша',
             'Дима', 'Евгений', 'Женя', 'Захар']

team_num = len(team_list)

for i in range(team_num):
    if i // 2 != i / 2:
        print(team_list[i])