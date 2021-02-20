'''
=-=-= Lab19 28 Jan 2021 =-=-=
=-=-=- BlackJackAdvice -=-=-=
=-=-=- Composer: brndn -=-=-=
'''

card_value = {    #dictionary of card values
    'a': 1,
    'ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'jack': 10,
    'q': 10,
    'queen': 10,
    'k': 10,
    'king': 10,
}

first = input("\nEnter first card: ").lower()
second = input("second card: ").lower()
third = input("Third card: ").lower()

total = card_value[first] + card_value[second] + card_value[third]    #use imputs to get total of corresponding values

if total < 17:            #compare total to determine advice
    adv = "Hit!"
elif 21 > total >= 17:
    adv = "Stay"
elif total == 21:
    adv = "Blackjack!"
else:
    adv = "Already Busted"

print(total, adv)