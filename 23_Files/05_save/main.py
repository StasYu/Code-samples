import os
text = input('Введите строку: ')

# Функция проверки пути
def existing(path):
    new_path = f"/{'/'.join(path)}"
    result = os.path.isdir(new_path)
    return result

# Основная функция
def saver(text):
    q_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ')
    q_name = input('Введите имя файла: ')
    q_path = q_path.split()
# Проверка пути:
    if not existing(q_path):
        print('Указанного пути не существует!')
        return None
# Создание директории:
    q_path.append(f'{q_name}.txt')
    final_path = '/'.join(q_path)
# Проверка наличия файла:
    if os.path.exists(f'/{final_path}'):
        # Функция перезаписи файла:
        question = int(input('Точно перезаписать файл? 1-Да/2-Нет '))

        if question == 1:
            result = open(f'/{final_path}', 'w')
            result.write(text)
            result.close()
            print('Файл успешно перезаписан!')
            return None

        elif question == 2:
            print('Процесс прерван!')
            return None
# Если создается новый файл выполняется функция
    result = open(f'/{final_path}', 'w')
    result.write(text)
    result.close()
    print('Файл успешно сохранён!')
    return None

l = saver(text)
