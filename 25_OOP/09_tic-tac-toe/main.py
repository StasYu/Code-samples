from tictactoe import Board, Player

def game(player_1, player_2, board):
    if not player_1.flag and not player_2.flag:
        board.borders()
        player_1.move()
    if not player_1.flag and not player_2.flag:
        board.borders()
        player_2.move()

board = Board()

player_1 = Player('X', board)
player_2 = Player('0', board)

while not player_1.flag and not player_2.flag:
    game(player_1, player_2, board)