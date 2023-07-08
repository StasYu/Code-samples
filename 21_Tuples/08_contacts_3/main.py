phonebook = {('Ксения', 'Мельникова'): 76876868, ('София', 'Иванова'): 1233211, ('Мария', 'Власова'): 132712973}

while True:
    quest = input('enter the action necessary: ').lower()

    if quest == 'добавить контакт':
        name = input('enter name and surname: ').split()
        name = tuple(name)

        if name in phonebook.keys():
            print('\nName is already exist in phonebook')

        number = int(input('enter phone number: '))
        phonebook[name] = number
        print(phonebook)

    elif quest == 'поиск человека по фамилии':
        surname = input('enter surname: ')

        for i in phonebook:
            if i[1] == surname:
                print('\n', i[0], i[1], phonebook[i])
