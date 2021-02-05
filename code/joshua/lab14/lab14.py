'''
Josh Novac
Lab 14
Python
PDX Code Guild
------------------------------------------------------------------------------------------------------
'''

import random

# defined function that generates 6 random numbers
def pick6():
    return [random.randint(1, 99) for x in range(6)]

# dictionary of number of matches and the winnings for each outcome of matching numbers
pool = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

# counters
count = 0
balance = 0
earnings = 0
expenses = 0

# loop for all 100,000 tickets
while count < 100000:

    winning_numbers = pick6()
    player_numbers = pick6()

    matching_numbers = 0
    for x in range(6):
        if player_numbers[x] == winning_numbers[x]:
            matching_numbers += 1

    balance += pool[matching_numbers]
    earnings += pool[matching_numbers]
    expenses += 2
    count += 1


# print final results of earnings, total spent, final balance, ROI, and number of matching numbers
print(f'\n\n\t   RECEIPT\n------------------------------')
print(f'WON: ${earnings:,}')
print(f'SPENT: ${expenses:,}')
print(f'CURRENT BALANCE: ${earnings - expenses:,}')
print(f'ROI: {(earnings - expenses) / expenses}\n------------------------------\n')
# print(f'Matching Numbers: {matching_numbers}')