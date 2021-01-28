# ---- Lab 19 ---- #

# - Blackjack with Advice - #

card_value = {
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'J' : 10,
    'Q' : 10,
    'K' : 10
}

print('What are the cards in your hand?')
card_1 = input('First card: ')
card_2 = input('Second card: ')
card_3 = input('third card: ')

def point_total(card_1, card_2, card_3):
    total = card_value[card_1] + card_value[card_2] + card_value[card_3]
    return total

points_IH = (point_total(card_1, card_2, card_3))
points_IH = int(points_IH)

def advice(points_IH):
    if points_IH <= 17:
        advice = 'You should HIT'
    elif 17 < points_IH < 21:
        advice = 'You should STAY'
    elif points_IH > 21:
        advice = 'You BUST!'
    elif points_IH == 21:
        advice = 'You Won! BLACKJACK!'
    return advice

print(f'Your total points in hand are: {points_IH}')
print(advice(points_IH))

# Optional part looks fun... I'll get there eventually. #