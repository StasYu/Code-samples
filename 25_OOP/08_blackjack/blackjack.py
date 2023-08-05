from random import randint
class Player:
    hand = 0

    def __init__(self, pack, name):
        self.name = name
        self.pack = pack

    def take(self):
        self.hand += self.pack.shuffle()


class Game:
    is_playing = True

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer

    def first_move(self):
        self.player.take()
        self.player.take()
        print(f'\n{self.player.name} score: {self.player.hand}\n')
        self.dealer.take()
        self.dealer.take()
        print(f'\n{self.dealer.name} score(#hidden): {self.dealer.hand}\n')

    def playing(self):
        if self.player.hand <= 21:
            move = input('take(1) or stop(2)? ')
            print()
            if move == '1' or move.lower() == 'take':
                self.player.take()
                self.dealer.take()
                print(f'\nPlayer score: {self.player.hand}')
                print(f'Dealer score(#hidden): {self.dealer.hand}\n')
            elif move == '2' or move.lower() == 'stop':
                print('Game over')
                self.is_playing = False
                self.scoring()
            else:
                print('wrong input')
                self.playing()
        else:
            self.is_playing = False
            self.scoring()

    def scoring(self):
        if self.player.hand > 21:
            if self.dealer.hand > 21:
                print("It's a draw, both overscorred")
            else:
                print('Player scored over 21, game over casino wins')
        elif self.player.hand <= 21:
            if self.player.hand == self.dealer.hand:
                print("It's a draw")
            elif self.player.hand < self.dealer.hand:
                if self.dealer.hand <= 21:
                    print('Player lose, casino wins')
                else:
                    print('Player wins! Congrats!')
            elif self.player.hand > self.dealer.hand:
                print('Player wins! Congrats!')


class Pack:
    pack = ('ace', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten',
            'jack', 'queen', 'king')
    full_pack = list(pack * 4)
    dispence = ''

    card = 0

    def __init__(self):
        self.count = 51

    def shuffle(self):
        random = randint(0, self.count)
        self.dispence = self.full_pack[random]
        self.full_pack.pop(random)
        self.count -= 1
        card = self.value()

        print(f'new card: {self.dispence}({card})')

        return card

    def value(self):
        if self.dispence == 'two':
            self.card = 2
        elif self.dispence == 'three':
            self.card = 3
        elif self.dispence == 'four':
            self.card = 4
        elif self.dispence == 'five':
            self.card = 5
        elif self.dispence == 'six':
            self.card = 6
        elif self.dispence == 'seven':
            self.card = 7
        elif self.dispence == 'eight':
            self.card = 8
        elif self.dispence == 'nine':
            self.card = 9
        elif self.dispence == 'ten' \
                or self.dispence == 'jack' \
                or self.dispence == 'queen' \
                or self.dispence == 'king':
            self.card = 10
        elif self.dispence == 'ace':
            self.card = 11
        return self.card
