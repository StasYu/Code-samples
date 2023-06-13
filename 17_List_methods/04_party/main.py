guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']




while True:
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    command = input('Гость пришел или ушел? ')
    name = input('Имя гостя: ')
    if command == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    elif command == 'пришел':
        if len(guests) < 6:
            print('Привет', name)
            guests.append(name)
        else:
            print('Прости,', name, 'но мест нет.')
    elif command == 'ушел':
        print('Пока,', name + '!')
        guests.remove(name)
    else:
        print('неверно введена команда')



