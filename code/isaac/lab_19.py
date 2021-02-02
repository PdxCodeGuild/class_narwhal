


cards = {
    'A':1,
    'K':10, 
    'Q':10, 
    'J':10,
    '10':10,
    '9':9,
    '8':8,
    '7':7,
    '6':6,
    '5':5,
    '4':4,
    '3':3,
    '2':2}


card_1 = input("Player what is your first card?  ")

card_2 = input("Player what is your second card?  ")

card_3 = input("Player what is your third card?  ")

total = (int(cards.get(card_1))) + (int(cards.get(card_2))) + (int(cards.get(card_3)))

hand_value = total 
    

while True:
    
    decision = ""

    if (hand_value) < 17:
        print(f"Hit! There is room to gamble, you have {total}")
        decision = input("What was your decision?" "Hit or Stay? ")
    
    elif (hand_value) >= 17 and hand_value <= 20:
        print(f"It would be best to stay, since you have {total}")
        decision = input("What was your decision?" "Hit or Stay? ")

    elif (hand_value) == 21:
        print("Black Jack! Looks like we have a winner")

    elif (hand_value) > 21:
        print("Busted! Sorry player the house wins")
        break 

    #if decision = Hit:
        #print(card_3)
        #total  += int(cards)
    

        

