# LAB 15 #

'''
>>> num_words = {     0 : 'Zero',     1 : 'One',     2 : 'Two',     3 : 'Three',     4 : 'Four',     5 : 'Five',     6 : 'Six',     7 : 'Seven',     8 : 'Eight',     9 : 'Nine'}
>>> num_words
{0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
>>> num_words[3]
'Three'
>>> num_words[8]
'Eight'
>>> 34 // 10
3
>>> 34 % 10
4
>>> 9 % 2
1
>>> 9 // 2
4
>>> 4.5 * 2
9.0
>>> number = 34
>>> tens = number // 10
>>> singles = number % 10
>>> tens
3
>>> singles
4
>>> num_words[singles]
'Four'
>>> tens_dict = {3: 'thirty'}
>>> tens_dict[tens]
'thirty'
>>> phrase = tens_dict[tens] + '-' + num_words[singles]
>>> phrase
'thirty-Four'
'''

# LAB 19 #

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
    total = card_1 + card_2 + card_3
    for card_1 in card_value:
        return card_value[card_1]
    for card_2 in card_value:
        return card_value[card_2]
    for card_3 in card_value:
        return card_value[card_3]
    return total

points_IH = (point_total(card_1, card_2, card_3))
points_IH = int(points_IH)

def advice(points_IH):
    if points_IH <= 17:
        advice = ' You should Hit'
    elif 17 < points_IH < 21:
        advice = 'You should Stay'
    elif points_IH > 21:
        advice = 'You Bust!'
    elif points_IH == 21:
        advice = 'Blackjack!'
    return advice

print(f'Your first card is: {card_1}')
print(f'Your second card is: {card_2}')
print(f'Your third card is: {card_3}')
print(f'Your total points in hand are: {points_IH}')
print(advice(points_IH))
