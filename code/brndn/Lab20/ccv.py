'''
=-=-= Lab20 29 Jan 2021 =-=-=
=- Credit Card Validation =-=
=-=-=- Composer: brndn -=-=-=
'''

card = input('\nEnter Card Number\n\n>>> ')

def ccv(card):

    card_num = [int(n) for n in card]

    check = card_num.pop()

    card_num.reverse()
    card_num[::2] = [n*2 for n in card_num[::2]]
    card_num = [n-9 if n>9 else n for n in card_num]
    card_num = sum(card_num) % 10

    if card_num == check:
        validity = "Valid!"
    else:
        validity = "Invalid!"

    return validity

print(f'\n{ccv(card)}\n')