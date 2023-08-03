class Warrior:
    health = 100
    is_dead = False

    def __init__(self, index):
        self.index = index

    def damage(self):
        self.health -= 20

        if self.health > 0:
            self.info()

        else:
            print(f'Player {self.index} is dead')
            self.is_dead = True

    def info(self):
        print(f'player {self.index}: {self.health} hp\n')


class Game:
    war_1 = Warrior(1)
    war_2 = Warrior(2)
    game_over = False

    def attack(self, coin):
        flag = self.is_dead()

        if not flag:

            if coin == self.war_1.index:
                print('player 2 attacked player 1')
                self.war_1.damage()

            else:
                print('player 1 attacked player 2')
                self.war_2.damage()

        else:
            self.game_over = True

    def is_dead(self):

        if self.war_1.is_dead:
            print('Player 2 won!')
            return True

        elif self.war_2.is_dead:
            print('Player 1 won!')
            return True
