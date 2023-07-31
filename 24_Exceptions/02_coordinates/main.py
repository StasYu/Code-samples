import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()

        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except:
            print("Что-то пошло не так с первой функцией")

        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except:
            print("Что-то пошло не так со второй функцией")

        number = random.randint(0, 100)

try:
        with open('result.txt', 'w') as file_2:
            my_list = sorted([res1, res2, number])
            print(my_list)
            for i in my_list:
                file_2.write(str(i))
                file_2.write('\n')
except:
    print('Что-то пошло не так')