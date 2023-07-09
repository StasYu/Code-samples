country_num = int(input('Кол-во стран: '))
country_dict = dict()
flag = True

for i_country in range(country_num):
    country_list = input(f'{i_country+1} страна: ').split()
    country_dict[country_list[0]] = country_list[1:4]

# print(country_dict)
for i_city in range(3):
    city = input(f'\n{i_city + 1} город: ')
    for j_country in country_dict:
        # print(j_country)
        if city in country_dict[j_country]:
            print(f'Город {city} расположен в стране {j_country}.')
            flag = False
    if flag:
        print(f'По городу {city} данных нет.')
    flag = True
