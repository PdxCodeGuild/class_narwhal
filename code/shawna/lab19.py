import time
print("""
Welcome to Blackjack Butler! I am here to give you advice based on your hand.\n
This is only advise, as I am sure you know, I can't promise you will win. \n
But I wish you luck!

Enter your card by it's number. For face cards enter J, Q, K, or A
""")
cards = {

   "1": 1,
   "2": 2,
   "3": 3,
   "4": 4,
   "5": 5,
   "6": 6,
   "7": 7,
   "8": 8,
   "9": 9,
   "10": 10,
   "J": 10,
   "Q": 10,
   "K": 10,
   "A": 1,
}

card1 = (input("What is the first card in your hand? "))
print("Okay, got it")
card2 = (input("What is the second card in your hand? "))
subtotal = (int(cards.get(card1))) + (int(cards.get(card2)))
hand = subtotal

while True:
        choice = ""

        if (hand) < 17:
            print(f"Hit! You only have a {hand}")
            choice = input("Did you hit or did you stay? Hit/Stay: " )
        elif 17 <= (hand) <= 20:
            print(f"Stay, {hand} is a pretty decent score")
            choice = input("Did you hit or did you stay? Hit/Stay: " )
        elif (hand) == 21:
            print("What are you looking to me for, you won! Congrats!")
            break
        elif (hand) > 21:
            print(f"Daw, looks like ya busted with a {hand}. Better luck next time!")
            break
        else:
            print("I am not sure that is a valid playing card. You trying to cheat?")
            break
        
        if choice == "hit":
            card = input("Please enter your new card: ")
            hand += int(card)
        else:
            print("I hope you won! I will be here if you would like my advice again.") 
            break   
