
def calculating_math_func(data, result={1:1}):
    if data in result:
        return result[data]
    temp = 1
    for index in range(1, data + 1):
        temp *= index
    temp /= data ** 3
    temp = temp ** 10
    result[data] = temp
    print(result)
    return result[data]
# Оптимизировал функцию чтобы не высчитывать результат
# того же числа, вместо факториала

while True:
    number = int(input('enter new num: '))
    print(f'first answer: {calculating_math_func(number)}')