from random import randint

class Home:
    food = 50
    money_box = 0

class Human:
    satiety = 50

    def __init__(self, home, name):
        self.home = home
        self.name = name

    def eat(self):
        self.satiety += 1
        self.home.food -= 1

    def work(self):
        self.satiety -= 1
        self.home.money_box += 1

    def play(self):
        self.satiety -= 1

    def shopping(self):
        self.home.food += 1
        self.home.money_box -= 1

    def daily_routine(self, day, roll):

        if self.satiety < 0:
            return None

        self.roll(day, roll)


    def roll(self, day, roll):

        if roll == 3:
            if self.satiety < 20:
                self.eat()

        elif roll == 4:
            if self.home.food < 10:
                self.shopping()

        elif roll == 5:
            if self.home.money_box < 50:
                self.work()

        elif roll == 6:
            self.play()

        elif roll == 1:
            self.work()

        elif roll == 2:
            self.eat()

        if self.satiety < 0:
            print(f'day {day}, {self.name} is dead')


home = Home()

tanent_1 = Human(home, 'Bob')
tanent_2 = Human(home, 'Tom')


for i_day in range(1, 366):

    dice_spin = randint(1, 6)
    tanent_1.daily_routine(i_day, dice_spin)

    dice_spin = randint(1, 6)
    tanent_2.daily_routine(i_day, dice_spin)