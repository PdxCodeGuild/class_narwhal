'''
Lab 14
Version 1
Pick 6
'''

import random

# Payout for matching numbers
pays = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}
balance = 0

# defined function to generate 6 numbers
def pick6():
    ticket = []
    for num in range(6):
        num = random.randint(1,99)
        ticket.append(num)
    return ticket

# defined function to get number of matches
def num_matches(winning,ticket):
    matching_nums = 0
    for x in range(len(winning)):
        if winning[x] == ticket[x]:
            matching_nums += 1
    return matching_nums

# identify winning nums
winning_nums = pick6()

# loop for 100,000
for x in range(100000):

    ticket_nums = pick6() # get ticket numbers
    matching_nums = num_matches(winning_nums,ticket_nums) # get matching numbers
    balance -= 2 # reduce $2 per ticket from balance
    balance += pays[matching_nums] # adds winnings to balance

print(f'Balance: ${balance}') # Final Balance
