from random import randint
class Home:
    def __init__(self, moneybox=100, food=50, cat_food=30, dirt=0):
        self.__moneybox = moneybox
        self.__food = food
        self.__cat_food = cat_food
        self.__dirt = dirt

    def info(self):
        print(f'HOME:\n'
              f'money: {self.__moneybox}\n'
              f'food: {self.__food}\n'
              f'cat food: {self.__cat_food}\n'
              f'dirt lvl: {self.__dirt}\n')

    def get_money(self):
        return self.__moneybox

    def get_food(self):
        return self.__food

    def get_cat_food(self):
        return self.__cat_food

    def get_dirt(self):
        return self.__dirt

    def set_money(self, money):
        self.__moneybox += money

    def set_food(self, food):
        self.__food += food

    def set_cat_food(self, cat_food):
        self.__cat_food += cat_food

    def set_dirt(self, dirt):
        self.__dirt += dirt


class Human:

    def __init__(self, house, name, sati=30, happy=100):
        self.__name = name
        self.__sati = sati
        self.__happy = happy
        self.__house = house
        self.__dead = False

    def action(self):
        self.__sati -= 10

    def pat(self):
        self.__happy += 5
        self.action()

    def is_hunger(self):
        if self.__sati <= 0:
            print(f'{self.__name} is dead from hunger!')
            self.__dead = True
            return True

    def is_depressed(self):
        if self.__happy <= 10:
            self.__dead = True
            return True

    def is_dirty(self):
        if self.__house.get_dirt >= 90:
            self.__happy -= 10

    def dead_check(self):
        if self.is_hunger() or self.is_depressed():
            return True


class Husband(Human):

    def __init__(self, house, name, sati=30, happy=100):
        self.__name = name
        self.__sati = sati
        self.__happy = happy
        self.__house = house
        self.__dead = False

    def info(self):
        print(f'name: {self.__name}'
              f'\nsatiety: {self.__sati}'
              f'\nhappiness: {self.__happy}\n')

    def action(self):
        self.__sati -= 10

    def pat(self):
        self.__happy += 5
        self.action()

    def is_hunger(self):
        if self.__sati <= 0:
            print(f'{self.__name} is dead from hunger!')
            self.__dead = True
            return True

    def is_depressed(self):
        if self.__happy <= 10:
            self.__dead = True
            return True

    def is_dirty(self):
        if self.__house.get_dirt >= 90:
            self.__happy -= 10

    def dead_check(self):
        if self.is_hunger() or self.is_depressed():
            return True

    def move(self):
        if self.__sati <= 10:
            self.eat()
        elif self.__happy <= 10:
            self.play()
        elif self.__house.get_money() <= 80:
            self.work()
        else:
            coin = randint(1, 4)

            if coin == 1:
                self.eat()
            elif coin == 2:
                self.play()
            elif coin == 3:
                self.work()
            else:
                self.pat()

        self.info()
        self.dead_check()

    def eat(self):
        print(f'eating...')
        if self.__house.get_food() > 60:
            self.__sati += 30
            self.__house.set_food(-30)

        elif self.__house.get_food() > 30:
            self.__sati += 15
            self.__house.set_food(-15)

        else:
            self.__house.set_food(-self.__house.get_food())
            self.__sati += self.__house.get_food()

    def play(self):
        print(f'playing...')
        self.action()
        self.__sati += 20

    def work(self):
        print('working...')
        self.action()
        self.__house.set_money(150)

class Wife(Human):
    def __init__(self, house, name, sati=30, happy=100):
        self.__name = name
        self.__sati = sati
        self.__happy = happy
        self.__house = house
        self.__dead = False

    def info(self):
        print(f'name: {self.__name}'
              f'\nsatiety: {self.__sati}'
              f'\nhappiness: {self.__happy}\n')

    def action(self):
        self.__sati -= 10

    def pat(self):
        print(f'pat...')
        self.__happy += 5
        self.action()

    def is_hunger(self):
        if self.__sati <= 0:
            print(f'{self.__name} is dead from hunger!')
            self.__dead = True
            return True

    def is_depressed(self):
        if self.__happy <= 10:
            self.__dead = True
            return True

    def is_dirty(self):
        if self.__house.get_dirt >= 90:
            self.__happy -= 10

    def dead_check(self):
        if self.is_hunger() or self.is_depressed():
            return True

    def move(self):
        if self.__sati <= 10:
            self.eat()
        elif self.__happy <= 10:
            if self.__house.get_money() < 350:
                self.pat()
            else:
                self.coat_buy()
        elif self.__house.get_food() <= 60:
            self.shopping()
        elif self.__house.get_dirt() >= 80:
            self.clean()
        else:
            coin = randint(1, 5)

            if coin == 1:
                self.eat()
            elif coin == 2:
                self.shopping()
            elif coin == 3:
                self.coat_buy()
            elif coin == 4:
                self.clean()
            else:
                self.pat()

        self.info()
        self.dead_check()

    def eat(self):
        print(f'eating...')
        if self.__house.get_food() >= 60:
            self.__sati += 30
            self.__house.set_food(-30)

        elif self.__house.get_food() >= 30:
            self.__sati += 15
            self.__house.set_food(-15)

        else:
            self.__house.set_food(-self.__house.get_food())
            self.__sati += self.__house.get_food()

    def shopping(self):
        print(f'shopping...')
        if self.__house.get_money() >= 105:
            self.__house.set_money(-105)
            self.__house.set_food(85)
            self.__house.set_cat_food(20)

        elif self.__house.get_money() >= 40:
            self.__house.set_money(-40)
            self.__house.set_food(30)
            self.__house.set_cat_food(10)

        else:
            self.__house.set_food(self.__house.get_money())
            self.__house.set_money(-self.__house.get_money())
        self.action()

    def coat_buy(self):
        print(f'buying new coat...')
        self.action()
        if self.__house.get_money() >= 350:
            self.__house.set_money(-350)
            self.__happy += 60

    def clean(self):
        print(f'cleaning...')
        self.action()
        if self.__house.get_dirt() >= 100:
            self.__house.set_dirt(-100)
        else:
            self.__house.set_dirt(-self.__house.get_dirt())

class Cat:
    def __init__(self, house, name, sati=30):
        self.__house = house
        self.__name = name
        self.__sati = sati
        self.__dead = False

    def info(self):
        print(f'\nname: {self.__name}\n'
              f'satiety: {self.__sati}\n')

    def dead_check(self):
        if self.__sati <= 0:
            print(f'{self.__name} is dead from hunger!')
            self.__dead = True
            return True

    def move(self):
        if self.__sati <= 10:
            self.eat()
        else:
            coin = randint(1, 4)

            if coin == 1:
                self.eat()
            elif coin == 2:
                self.sleep()
            elif coin == 3:
                self.rage()
        self.info()
        self.dead_check()


    def eat(self):
        print('eating...')
        if self.__house.get_cat_food() >= 10:
            self.__sati += 20
            self.__house.set_cat_food(-10)

        elif self.__house.get_food() >= 5:
            self.__sati += 10
            self.__house.set_cat_food(-5)

        else:
            self.__house.set_cat_food(-self.__house.get_cat_food())
            self.__sati += 2 * self.__house.get_cat_food()

    def sleep(self):
        print('sleeping...')
        self.action()

    def rage(self):
        print('tear wallpaper')
        self.action()
        self.__house.set_dirt(5)

    def action(self):
        self.__sati -= 10


home = Home()
wife = Wife(name='Sara',house=home)
husband = Husband(name='Bill', house=home)
cat = Cat(name='Snow', house=home)

for i_day in range(1, 366):
    print(f'\nDay {i_day}:')
    home.info()
    wife.move()
    husband.move()
    cat.move()

