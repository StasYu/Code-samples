# generation = {'Alexei': 'Peter_I',
#               'Anna': 'Peter_I',
#               'Elizabeth': 'Peter_I',
#               'Peter_II': 'Alexei',
#               'Peter_III': 'Anna',
#               'Paul_I': 'Peter_III',
#               'Alexander_I': 'Paul_I',
#               'Nicholaus_I': 'Paul_I'}

human_num = int(input('Введите количество человек: '))
generation = dict()

for i_hum in range(1, human_num):
    pair = input(f'{i_hum} пара: ').split()
    generation.update({pair[0]:pair[1]})


for i in generation.values():
    if i not in generation.keys():
        parent = [i]

legacy_dict = {parent[0]: 0}
temp = list()
count = 1
# print('parent: ', parent)
while count < len(set(generation)):
    for i in parent:
        for j in generation:
            if generation.get(j) == i:
                temp.append(j)
                legacy_dict.update({j: count})
    count += 1
    parent = temp
    temp = list()

sorted_legacy_dict = dict(sorted(legacy_dict.items()))

print('Высота” каждого члена семьи:')
for i in sorted_legacy_dict:
    print(i, sorted_legacy_dict.get(i))