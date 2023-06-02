films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
check = 0
favorite_list = []

while True:
    favorite = input('Введите название фильма: ')
    for i in films:
        if favorite == i:
            check = 1
            favorite_list.append(i)
    if check != 1:
        print('Ошибка')
        break
    check = 0

print('список любимых фильмов: ', favorite_list)


