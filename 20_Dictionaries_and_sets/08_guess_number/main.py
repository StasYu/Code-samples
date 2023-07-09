max_num = int(input('Введите максимальное число: '))
num_list = {str(i):'blank' for i in range(1, max_num + 1)}
print(num_list)
question = ''

while question != 'Помогите!':
    question = input('Нужное число есть среди вот этих чисел: ')
    if question == 'Помогите!':
        break
    question_list = question.split()

    answer = input('Ответ Артёма: ')
    for i_num in question_list:
        if answer == 'Да' and num_list.get(i_num) == 'blank':
            num_list.update({i_num: answer})
        elif answer == 'Нет':
            num_list[i_num] = answer
    answer = 'blank'

print('Артём мог загадать следующие числа: ', end='')
for i in num_list:
    if num_list.get(i) == 'Да':
        print(i, end=' ')