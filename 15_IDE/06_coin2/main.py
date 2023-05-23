import math
print('Введите координаты монетки:')
x_num = float(input('x: '))
y_num = float(input('y: '))

radius = float(input('Введите радиус: '))

distance = math.sqrt(((x_num - 0)** 2) + ((y_num - 0) ** 2))

if distance <= radius:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')