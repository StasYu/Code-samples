from math import sin, tan, radians

class Car:
    """
    Класс автомобиль

    arguments:
        __x = положение по оси x
        __y = положение по оси y
        __distance = расстояние которое проехал
        __angle = направление(угол) в котором авто двигается
        (о градусов: условные "на 12 часов", 90 градусов "на 3 часа")
    """
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__distance = 0
        self.__angle = 0

    def get_distance(self):
        """

        :return:
            rtype(float) - move distance
        """
        return self.__distance

    def move(self):
        """
        function for one drive
        angle(int): direction where we're moving in degrees in range(0-360)
        distance(float): distance that we're drive at one move

        if/else construction:
            if angle = 0, 90, 180, 270 we moving only on x or y axis
            else we call "def points" that calculates new x and y position
        """
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
        """
        function for calculating x and y position based on direction(angle)
        result - we're changing __x and __y arghs


        :param distance: __distance = расстояние которое проехал
        :param angle: __angle = направление(угол) в котором авто двигается

        """
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
        """

        :param distance: __distance = расстояние которое проехал
        :param angle: __angle = направление(угол) в котором авто двигается
        :return: True or False if angle = 0, 90, 180, 270
        if True we moving only on x or y axis
        else return False
        """
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
        """function that shows info about car position"""
        print(f'car driving at point x:{self.__x}, y:{self.__y}')

    def katets(self, angle, distance):
        """
        subfunction that calculate katet_1 and katet_2 equal to new x or y position on axis
        :param distance: __distance = расстояние которое проехал
        :param angle: __angle = направление(угол) в котором авто двигается

        """
        self.__katet_1 = sin(angle) * distance
        self.__katet_2 = tan(90 - angle) * abs(self.__katet_1)

class Bus(Car):
    """
    subclass: Bus
    parental classs: Car
    """
    def __init__(self, x=0, y=0, passenger=0, money=0):
        """

        :param x: position on axis x
        :param y:position on axis y
        :param passenger: q-ty of passenger (by default = 0)
        :param money:amount of money (by default  = 0)
        """
        super().__init__(x=0, y=0)
        self.__passenger = passenger
        self.__money = money

    def enter(self, passenger):
        """

        :param passenger: q-ty of passenger that entering a bus
        :return: changing __passenger
        """
        self.__passenger += passenger

    def exit(self, passenger):
        """

        :param passenger: q-ty of passenger that leaving bus
        :return: changing __passenger
        """
        self.__passenger -= passenger

    def move(self):
        """
        copying parental function move
        changing money amount based on __passenger * distance
        """
        super().move()
        self.__money += self.__passenger * self.get_distance()

    def info(self):
        """
        copying parental function info
        changes: printing amount of passengers in bus and money box
        """
        super().info()
        print(f'passenger in bus: {self.__passenger}\nmoney in box: {self.__money}\n')

new_bus = Bus()
new_bus.enter(8)
new_bus.exit(3)

try:
    while True:
        new_bus.move()
except:
    print('\n\nTour is over')