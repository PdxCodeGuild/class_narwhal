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
winning_nums = []
balance = 0
loop_count = 0 # loop 100,000 times
ticket_nums = []
cost = 2
win = 0
match_nums = 0


def pick6():
    num = random.randint(1,99)
    return num




while loop_count < 100000:

    for w in range(6):
        w = pick6()
        winning_nums.append(w)

    for t in range(6):
        t = pick6()
        ticket_nums.append(t)

    cost =+ 2
    balance -= 2
    loop_count += 1

    if winning_nums == ticket_nums:
        match_nums += 1

    win += pays[match_nums]
    balance += pays[match_nums]

print(f'${balance}') # Final Balance
