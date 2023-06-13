violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

total_lenght = 0

while True:
    amount_songs = int(input('\nСколько песен выбрать? '))
    for i_amount in range(amount_songs):
        print('Название', i_amount + 1, 'песни: ', end = ' ')
        name_song = input('')

        for i_songs in violator_songs:
            if name_song == i_songs[0]:
                total_lenght += i_songs[1]
    print('Общее время звучания песен: ', round(total_lenght, 2), 'минут' )
