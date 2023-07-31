def operations(values, total):
    operands = values.split()
    if operands[1] == '+':
        operation = int(operands[0]) + int(operands[2])
    elif operands[1] == '-':
        operation = int(operands[0]) - int(operands[2])
    elif operands[1] == '*':
        operation = int(operands[0]) * int(operands[2])
    elif operands[1] == '/':
        operation = int(operands[0]) / int(operands[2])
    elif operands[1] == '//':
        operation = int(operands[0]) // int(operands[2])
    elif operands[1] == '%':
        operation = int(operands[0]) % int(operands[2])
    total += operation
    return total

temp = 0

with open('calc.txt', 'r') as calc_file:
    with open('calc2.txt', 'w+') as temp_file:

        for i_line in calc_file:
            try:
                temp = operations(i_line, temp)
                temp_file.write(i_line)

            except:
                error = i_line.replace('\n', '')
                question = input(f'Обнаружена ошибка в строке: {error} Хотите исправить? ')

                if question.lower() == 'да':
                    cor_result = input('Введите исправленную строку: ')
                    try:
                        temp = operations(cor_result, temp)
                        new = i_line.replace(error, cor_result)
                        temp_file.write(new)
                    except:
                        print('Неверный ввод')
                        temp_file.write(i_line)
                else:
                    temp_file.write(i_line)
        temp_file.seek(0)
        content = temp_file.read()


with open('calc.txt', 'w') as file:
    file.write(content)

print(f'Сумма результатов: {temp}')
