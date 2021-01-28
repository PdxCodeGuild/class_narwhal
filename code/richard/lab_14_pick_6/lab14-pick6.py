# Lab 14: Pick6
# Richard
# January 28th, 2021
'''
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. 
Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and 
the number of matches between the ticket and the winning numbers determines the payoff. 
Order matters, if the winning numbers are `[5, 10]` and your ticket numbers are `[10, 5]` you have **0** matches. 
If the winning numbers are `[5, 10, 2]` and your ticket numbers are `[10, 5, 2]`, you have **1** match. 
Calculate your net winnings (the sum of all expenses and earnings).

- a ticket costs $2
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000

One function you might write is `pick6()` which will generate a list of 6 random numbers, 
which can then be used for both the winning numbers and tickets. 
Another function could be `num_matches(winning, ticket)` 
which returns the number of matches between the winning numbers and the ticket.


'''
## Steps

# 1. Generate a list of 6 random numbers representing the winning tickets

import random
winning_1 = random.randint(1, 99)
winning_2 = random.randint(1, 99)
winning_3 = random.randint(1, 99)
winning_4 = random.randint(1, 99)
winning_5 = random.randint(1, 99)
winning_6 = random.randint(1, 99)

winning_tickets = (winning_1, winning_2, winning_3, winning_4, winning_5, winning_6)
print(f"winning ticket: {winning_tickets}")



# 2. write functions that I will need


def buy_ticket():

    random1 = random.randint(1, 99)
    random2 = random.randint(1, 99)
    random3 = random.randint(1, 99)
    random4 = random.randint(1, 99)
    random5 = random.randint(1, 99)
    random6 = random.randint(1, 99)
    return [random1, random2, random3, random4, random5, random6]

def compare_ticket(my_ticket, winning_ticket):
    count = 0
    if my_ticket[0] == winning_ticket[0]:
        count += 1
    if my_ticket[1] == winning_ticket[1]:
        count += 1
    if my_ticket[2] == winning_ticket[2]:
        count += 1
    if my_ticket[3] == winning_ticket[3]:
        count += 1
    if my_ticket[4] == winning_ticket[4]:
        count += 1
    if my_ticket[5] == winning_ticket[5]:
        count += 1
    return count


'''
- if 1 number matches, you win $4
- if 2 numbers match, you win $7
- if 3 numbers match, you win $100
- if 4 numbers match, you win $50,000
- if 5 numbers match, you win $1,000,000
- if 6 numbers match, you win $25,000,000
'''

def calc_payout(matches):
    if matches == 1:
        payout = 4
    elif matches == 2:
        payout = 7
    elif matches == 3:
        payout = 100
    elif matches == 4:
        payout = 50000
    elif matches == 5:
        payout = 1000000
    elif matches == 6:
        payout = 25000000
    else:
        payout = 0
    return payout


# my_ticket = buy_ticket()
# print(f"Ticket 1: {my_ticket}")
# print(compare_ticket(my_ticket, winning_tickets))



# 3. Solve the problem
'''
2. Loop 100,000 times, for each loop:
3. Generate a list of 6 random numbers representing the ticket
4. Subtract 2 from your balance (you bought a ticket)
5. Find how many numbers match 
6. Add to your balance the winnings from your matches
7. After the loop, print the final balance
'''

balance = 0
times = 100000
count = 0
matches = 0
total_winnings = 0

for each_attempt in range(times):
    balance = balance - 2
    my_ticket = buy_ticket()
    matches = compare_ticket(my_ticket, winning_tickets)
    count += matches
    winnings = calc_payout(matches)
    total_winnings += winnings

# calculate total amount of money lost
amount_lost = - balance - total_winnings


# Display the output
print(f"You bought {times} tickets. That cost you {-balance}. You had {count} matched numbers.")
print(f"Your total winnings were {total_winnings}")
print(f"You lost {amount_lost} dollars")






'''

## Version 2

The ROI (return on investment) is defined as `(earnings - expenses)/expenses`. 
Calculate your ROI, print it out along with your earnings and expenses.
'''