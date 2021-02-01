'''
Lab 14
Version 1
Pick 6
'''


''' --------------------Merrit's in-class Sample---------------------------------------------
import random

def pick6(): #Step 1
    return [random.randint(1,99) for x in range(6)]
    # ticket = []
    # for x in range(6):
    #     ticket.append(random.randint(1,99))
    #     return ticket


def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

# def num_matches(winning, ticket):
#     matches = 0
#     for num in ticket:
#         if num in winning:
#             matches += 1
#     return matches

winnings = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

balance = 0 #Step 2
earnings = 0
expenses = 0

number_of_matches = [0, 0, 0, 0, 0, 0]

winning_ticket = pick6()

for n in range(100000): # Step 3
    current_ticket = pick6() # Step 4
    balance -= 2 # Step 5
    expenses += 2
    matches = num_matches(winning_ticket, current_ticket) # Step 6
    balance += winnings[matches] # Step 7
    earnings += winnings[matches]
    number_of_matches[matches] += 1

print("Balance: ", balance) # Step 8
print("Expenses: ", expenses)
print("Earnings: ", earnings)
print("ROI: ", (earnings - expenses)/expenses)
for i, num in enumerate(number_of_matches):
    print(i, num)


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
