# Lab 19: Blackjack Advice
# Richard
# January 28th, 2021

'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 

Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. 

At this point, assume aces are worth 1. Use the following rules to determine the advice:

'''

# 1. Ask the user for the 3 playing cards
print("Tell me your cards - A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K ")
card1 = input("What's your first card? ")
card2 = input("What's your second card? ")
card3 = input("What's your third card? ")

# 2. Figure out the point values of each card

def count_points(card):
    if card == "A":
        points = 1
    elif card == "2":
        points = 2
    elif card == "3":
        points = 3
    elif card == "4":
        points = 4
    elif card == "5":
        points = 5
    elif card == "6":
        points = 6
    elif card == "7":
        points = 7
    elif card == "8":
        points = 8
    elif card == "9":
        points = 9
    else:
        points = 10
    
    return points

print(f"card 1: {card1}:{count_points(card1)} points")
print(f"card 2: {card2}:{count_points(card2)} points")
print(f"card 3: {card3}:{count_points(card3)} points")



# 3. Give Advice
'''
* Less than 17, advise to "Hit"
* Greater than or equal to 17, but less than 21, advise to "Stay"
* Exactly 21, advise "Blackjack!"
* Over 21, advise "Already Busted"

Print out the current total point value and the advice.
'''
total_points = count_points(card1) + count_points(card2) + count_points(card3)

print(f"Your total points are: {total_points}")

def advice(points):
    if points < 17:
        advice = "Hit"
    elif points == 21:
        advice = "Blackjack!"
    elif points > 21:
        advice = "Already Busted"
    else:
        advice = "Stay"
    return advice

advice = advice(total_points)

print(f"Your advice is: {advice}")   



'''
What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
'''








'''
## Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both cards over 21. 
Remember that you can have multiple aces in a hand. 
Try generating a list of all possible hand values by doubling the number of values in the output 
whenever you encounter an ace. 
For one half, add 1, for the other, add 11. 
This ensures if you have multiple aces that you account for the full range of possible values.
'''