def blackjack(x,y,z):
    s = x+y+z
    if s <= 21:
        print(s)
    elif 11 in [x,y,z] and s > 21:
        print((s)-10)
    else:
        print('BUST')

    


blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)
