file = open('people.txt', 'r')
count = 0
total = 0

for i_line in file:
    try:
        count += 1
        if i_line.endswith('\n'):
            temp = len(i_line) - 1
        else:
            temp = len(i_line)
        if temp < 3:
            raise BaseException
        total += temp
    except BaseException:
        print(f'Строка ошибки: {count}', 'Слишком короткое имя')
        log_name = (f'Строка ошибки: {count}, Слишком короткое имя \n')
        with open('errors.log', 'a') as error_file:
            error_file.write(str(log_name))

print(total)
