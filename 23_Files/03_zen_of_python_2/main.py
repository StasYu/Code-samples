import string

file = open('zen.txt', 'r')
line_count = 0
word_count = 0
let_count = 0
flag = False


for i_line in file:
    line_count += 1
    line = i_line.split()

    for i_word in line:
        for i_let in i_word:

            if i_let in string.ascii_letters:
                let_count += 1
                flag = True

        if flag == True:
            word_count += 1
        flag = False
        
print(f'Количество букв: {let_count}')
print(f'Количество слов: {word_count}')
print(f'Количество строк: {line_count}')