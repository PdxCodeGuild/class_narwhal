card_one = input("What is your first card? (A, 2-10, J, Q, K): ")
card_two = input("What is your second card? (A, 2-10, J, Q, K): ")
card_three = input("What is your third card? (A, 2-10, J, Q, K): ")

cards = [card_one, card_two, card_three]

counter = 0
# for ard in cards:
#     if card == "A":
#         counter += 1
#     elif card in ["J", "Q", "K"]:
#         counter += 10
#     elif 2 <= int(card) <= 10:
#         counter += int(card)

card_values = {
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

for card in cards:
    counter += card_values.get[card] if card_values.get[card] != None else 0


if counter < 17:
    print(f"{counter} Hit")
elif 17 <= 21:
    print(f"{counter} Stay")
elif counter == 21:
    print(f"{counter} Blackjack!")
elif counter > 21:
    print(f"")