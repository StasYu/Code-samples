import random
f_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
s_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners_list = [f_team[i_num] if f_team[i_num] > s_team[i_num]
                else s_team[i_num]
                for i_num in range(20)]


print('Первая команда: ', f_team)
print('Вторая команда: ', s_team)
print('Победители тура:  ', winners_list)