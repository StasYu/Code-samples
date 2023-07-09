people = {('Сидоров', 'Никита'): 35, ('Сидорова', 'Алина'): 34, ('Сидоров', 'Павел'): 10,
            ('Мельникова', 'Ксения'): 30, ('Иванова', 'София'): 23, ('Иванов','Иван'): 25}

surname = input(f'Введите фамилию: ').title()
print()

if surname[len(surname) - 1] == 'а':
    surname = surname[:len(surname) - 1]

for i_name, i_age in people.items():
    if surname in i_name[0]:
        print(i_name[0],i_name[1], i_age)