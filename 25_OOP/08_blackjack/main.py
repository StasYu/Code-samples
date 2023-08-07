from blackjack import*

pack = Pack()
player = Player(pack, 'Player')
dealer = Player(pack, 'Dealer')
game = Game(player, dealer)

game.first_move()
while game.is_playing:
    game.playing()