first_file = open('first_tour.txt', 'r')
second_file = open('second_tour.txt', 'w')

count = 0
second = str()

for i_line in first_file:
    line = i_line.split()

    if len(line) == 1:
        temp = int(i_line)

    else:
        if int(line[2]) > temp:
            count += 1
            second += f'{count}) ' \
                      f'{str(line[1])[0]}. ' \
                      f'{line[0]} ' \
                      f'{line[2]}\n'

second_file.write(f'{count}\n')
second_file.write(second)

first_file.close()
second_file.close()

second_file = open('second_tour.txt', 'r')
print(second_file.read())
