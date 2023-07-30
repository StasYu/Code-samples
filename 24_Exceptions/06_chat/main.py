file = open('chat.txt', 'a')
file.close()

while True:
    user_name = input('Введите имя пользователя: ')
    while True:
        question = input('Введите команду: \n'
                         '1 - Посмотреть текущий текст чата\n'
                         '2 - Отправить сообщение \n'
                         '3 - Сменить пользователя\n')
        try:
            if question == '1':
                with open('chat.txt', 'r') as file:
                    for i_line in file:
                        print(i_line)
            elif question == '2':
                text = input('Сообщение: ')
                with open('chat.txt', 'a') as file:
                    file.write(user_name)
                    file.write(': ')
                    file.write(text)
                    file.write('\n')
            elif question == 'Сменить пользователя' or question == '3':
                raise UserWarning
            else:
                raise SyntaxError
        except SyntaxError:
            print('Введите верную команду')
        except UserWarning:
            break
        except:
            print('Возникла непредвиденная ошибка, попробуйте еще раз')