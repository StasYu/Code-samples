from math import pi, sqrt

class Circle:
    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        self.squ = pi * self.r ** 2
        self.squ = round(self.squ, 2)
        print(f'square: {self.squ}')
        return self.squ

    def perimetr(self):
        perim = 2 * pi * self.r
        perim = round(perim, 2)
        print(f'perimeter: {perim}')
        return perim

    def grow(self, count):
        increase = self.squ * count
        increase = round(increase, 2)
        print(f'increased square: {increase}')
        return increase

    def is_cross(self, new_circle):
        d = sqrt(((self.x - new_circle.x) ** 2) + ((self.y - new_circle.y) ** 2))
        if d <= (self.r + new_circle.r):
            print('is circles crossed: True')
            return True
        print('circles is not crossed')
        return False