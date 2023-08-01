from random import randint
from game import Game

game = Game()

while not game.game_over:
    coin = randint(1,2)
    game.attack(coin)