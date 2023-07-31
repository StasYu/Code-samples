def operations(operands):
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
    return operation

temp = 0

with open('calc.txt', 'r') as calc_file:
    for i_line in calc_file:
        operands = i_line.split()
        try:
            result = operations(operands)
            temp += result
        except ValueError:
            print('Введите число')
        except SyntaxError:
            print('Syntax Error')
        except UnboundLocalError:
            print('Не введено действие')
        except IndexError:
            print('Не хватает строк')

print(temp)