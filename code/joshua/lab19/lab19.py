'''
Josh Novac
Lab 19
Python
PDX Code Guild
'''


'''
Version 1 --------------------------------------------------------------------
'''
# dictionary of each card and their values
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

# user inputs for each card.
# .title() if user enters lowercase letters for face cards
first_card = input('What is your first card? ').title()
sec_card = input('What is your second card? ').title()
third_card = input('What is your third card? ').title()

# adding hand total from each card (1st + 2nd + 3rd)
hand = cards[first_card] + cards[sec_card] + cards[third_card]

# rules for each combination
if hand < 17:
    print(f'{hand} ; Low hand, hit. ')
elif hand >= 17 and hand < 21:
    print(f'{hand} ; I would choose to stay. ')
elif hand == 21:
    print(f'{hand} ; Blackjack! ')
elif hand > 21:
    print(f'{hand} ; Already Busted. You went over 21. ')