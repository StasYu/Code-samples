class Board:
    num_list = [i for i in range(1, 10)]
    count = 1

    def borders(self):
        for i_num in range(1, 4):
            for j_num in range(self.count, self.count + 3):
                print('|{}|'.format(
                    self.num_list[j_num - 1]
                ), end='')
            print()
            self.count += 3
        self.count = 1

class Player:

    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.flag = False

    def move(self):
        request = input(f'{self.name} make your move: ')
        temp = int(request) - 1

        if isinstance(self.board.num_list[temp], int):
            self.board.num_list.pop(temp)
            self.board.num_list.insert(temp, self.name)
            self.is_game()
            # print(self.board.num_list)
        else:
            print('Field already filled')
            self.move()

    def is_winner(self, first, second, third):

        if self.board.num_list[first] == self.name:
            if self.board.num_list[second] == self.name:
                if self.board.num_list[third] == self.name:
                    return True
        else:
            return False

    def is_game(self):
        if self.is_winner(0, 1, 2) \
                or self.is_winner(3, 4, 5) \
                or self.is_winner(6, 7, 8) \
                or self.is_winner(0, 4, 8) \
                or self.is_winner(2, 4, 6) \
                or self.is_winner(0, 3, 6) \
                or self.is_winner(1, 4, 7) \
                or self.is_winner(2, 5, 8):
            print(f'\n{self.name} winner')
            self.flag = True