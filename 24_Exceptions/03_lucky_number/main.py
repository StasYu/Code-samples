import random

num = 0

while num < 777:
     num = int(input('Введите число: '))

     if random.randint(1,13) == 13:
         raise BaseException('Программа крашнулась')

     with open('new_file.txt', 'a') as file:
         file.write(str(num))
         file.write('\n')