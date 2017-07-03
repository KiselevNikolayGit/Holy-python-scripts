import random as rnd
cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
power = [2,3,4,5,6,7,8,9,10,10,10,10,11]
print (u'♣-♠-Зарубим в Блэк Джек?-♥-♦')
print ('')
global hand
hand = 0
game = ''
haveace = False

def sparing(x):
    res = rnd.randrange(15, 24)
    if x > 21:
        print (u'Да ты перебрал!')
        print ('!ПРОИГРЫШ!')
    elif res > 21:
        print (u'У тебя %d' % x)
        print (u'а Джек слегка перебрал')
        print ('!ПОБЕДА!')
    elif res == x:
        print (u'У тебя %d' % x)
        print (u'а вы не Джек, но очков у вас равно!')
        print ('!НИЧЬЯ!')
    elif res > x:
        print (u'У тебя %d' % x)
        print (u'а у Джека %d очков, вы слили.' % res)
        print ('!ПРОИГРЫШ!')
    elif res < x:
        print (u'У тебя %d' % x)
        print (u'а у Джека %d очков, а у вас больше!' % res)
        print ('!ПОБЕДА!')
    else: print (u'игра не зашла!')
    print ('')
    print (u'♣-♠-Играем еще-♥-♦')
    print ('')

while True:
    if hand == 0:
        game = input(u'Начнем? y/n   ')
    else: game = input(u'Мб, еще карту? y/n   ')
    if game == u'y':
        v = rnd.randrange(0,12,1)
        choice = cards[v]
        choice = rnd.choice (['♥','♦','♣','♠']) + choice
        hand += power[v]
        print (choice)
        print (('сила:' + str(power[v])) + ('   всего:' + str(hand)))
        if cards[v] == 'A':
            haveace = True
        if hand > 21:
            if not haveace:
                sparing (hand)
                hand = 0
                game = ''
            else: hand -= 10
    elif game == u'n':
        sparing (hand)
        hand = 0
        game = ''
