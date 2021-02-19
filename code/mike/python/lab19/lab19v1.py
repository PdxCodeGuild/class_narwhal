'''
Lab 19
Version 1
Blackjack Advice
'''

card_value= {
    'A' : 1,
    'K' : 10,
    'Q' : 10,
    'J' : 10,
    '10' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2
}

def calc_func(a, b, c):
    return (a + b + c)

card1 = input('What is your first card? ').upper()
card2 = input('What is your second card? ').upper()
card3 = input('What is your third card? ').upper()

c1 = card_value[card1]
c2 = card_value[card2]
c3 = card_value[card3]

total = calc_func(c1, c2, c3)

if total < 17:
    print(f'{total} Hit')
elif total >= 17 and total < 21:
    print(f'{total} Stay')
elif total == 21:
    print(f'{total} Blackjack!')
elif total > 21:
    print(f'{total} Already Busted')