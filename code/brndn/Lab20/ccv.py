'''
=-=-= Lab20 29 Jan 2021 =-=-=
=- Credit Card Validation =-=
=-=-=- Composer: brndn -=-=-=
'''

card = input('\nEnter Card Number\n\n>>> ')

def ccv(card):

    card_num = [int(n) for n in card]                   #turn elements in list into integers

    check = card_num.pop()                              #remove and store last digit as check

    card_num.reverse()                                  #reverse order
    card_num[::2] = [n*2 for n in card_num[::2]]        #double every other number
    card_num = [n-9 if n>9 else n for n in card_num]    #subtract 9 from numbers > 9
    card_num = sum(card_num) % 10                       #add the numbers together
                                                        #modulus 10 to get last digit of sum
    if card_num == check:                               #compare sum digit to check digit
        validity = "Valid!"
    else:
        validity = "Invalid!"

    return validity

print(f'\n{ccv(card)}\n')