import random
import time

def result(res_game, comp, play):
    decoding_res = dict(
        к = 'Камень',
        е = 'Бумага',
        н = 'Ножницы',
    )
    
    print('Соперник: ' + decoding_res[comp])
    print('Вы взяли: ' + decoding_res[play])

    if res_game == 'l':
        print('Ты проиграл бой, но не войну')
    elif res_game == 'w':
        print('Ты выиграл бой!')
    elif res_game == 'd':
        print('Ты не выграл, но и не проиграл!')
    else: pass
    
    time.sleep(3)

    for useless in range(7):
        print('')

def newgame():
    print('Здравствуй, сыграем в Камень - Ножницы - Бумага')
    player = input('Выбирайте мудро\nк - Камень\nе - Бумага\nн - Ножницы\n\nВаш выбор:')
    values_in = ['к', 'е', 'н']
    if values_in.count(player) == 1:
        comp_value = random.randrange(0, 3)
        player_value = values_in.index(player)
        if comp_value == player_value:
            result('d', values_in[comp_value], player)
        elif comp_value < player_value:
            if player_value == 2 and comp_value == 0:
                result('l', values_in[comp_value], player)
            else:
                result('w', values_in[comp_value], player)
        elif player_value < comp_value:
            if comp_value == 2 and player_value == 0:
                result('w', values_in[comp_value], player)
            else:
                result('l', values_in[comp_value], player)
        else: print('С вами что-то не так')
    else:
        print('А ты точно хочешь играть?')

while True:
    newgame()
