cargo_list = []
new_cargo_list = []
number_of_cargo = int(input('Кол-во контейнеров: '))
count = 0

for _ in range(number_of_cargo):
    weight_cargo = input('Введите вес контейнера: ')
    cargo_list.append(weight_cargo)

#print(cargo_list)
new_cargo = int(input('Введите вес нового контейнера: '))

for i in cargo_list:
    count += 1
    if new_cargo > int(i):
        break
print('Номер, куда встанет новый контейнер: ', count)