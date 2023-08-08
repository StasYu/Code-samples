from math import sin, tan, radians

class Car:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__distance = 0
        self.__angle = 0

    def get_distance(self):
        return self.__distance

    def move(self):
        angle = int(input('Enter angle in degrees(0-360): '))

        if angle < 0 or angle > 360:
            raise Exception('wrong angle\n')
        else:
            self.__angle = angle

        distance = float(input('Input distance in kilometres: '))
        self.__distance = distance


        if self.is_zero(distance=distance, angle=angle):
            self.info()
            return None
        else:
            self.points(angle=angle, distance=distance)
        self.info()

    def points(self, distance, angle):
        if angle > 270:
            new_angle = angle - 270
            self.katets(distance=distance, angle=radians(new_angle))
            self.__y += self.__katet_1
            self.__x -= self.__katet_2
        elif angle > 180:
            new_angle = angle - 180
            self.katets(distance=distance, angle=radians(new_angle))
            self.__x -= self.__katet_1
            self.__y -= self.__katet_2
        elif angle > 90:
            new_angle = angle - 90
            self.katets(distance=distance, angle=radians(new_angle))
            self.__y -= self.__katet_1
            self.__x += self.__katet_2
        elif angle < 90:
            new_angle = angle
            self.katets(distance=distance, angle=radians(new_angle))
            self.__x += self.__katet_1
            self.__y += self.__katet_2

    def is_zero(self, distance, angle):
        if angle == 0:
            self.__y += distance
            return True
        if angle == 90:
            self.__x += distance
            return True
        elif angle == 180:
            self.__y -= distance
            return True
        elif angle == 270:
            self.__x -= distance
            return True

    def info(self):
        print(f'car driving at point x:{self.__x}, y:{self.__y}')

    def katets(self, angle, distance):
        self.__katet_1 = sin(angle) * distance
        self.__katet_2 = tan(90 - angle) * abs(self.__katet_1)

class Bus(Car):
    def __init__(self, x=0, y=0, passenger=0, money=0):
        super().__init__(x=0, y=0)
        self.__passenger = passenger
        self.__money = money

    def enter(self, passenger):
        self.__passenger += passenger

    def exit(self, passenger):
        self.__passenger -= passenger

    def move(self):
        super().move()
        self.__money += self.__passenger * self.get_distance()

new_bus = Bus()
new_bus.enter(8)
new_bus.exit(3)

try:
    while True:
        new_bus.move()
except:
    print('\n\nTour is over')