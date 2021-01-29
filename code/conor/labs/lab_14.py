# ---- Lab 14 ---- #

# - Pick 6 - #

import random

def pick_6():
    rand_list = [random.randint(1, 99) for _ in range(6)]
    return rand_list

winning = pick_6()
print(winning)

def user_ticket():
    ticket = pick_6()
    return ticket

user = user_ticket()
print(user)

def comp_tickets(user_ticket, pick_6):
    count = 0
    if user_ticket[0] == pick_6[0]:
        count += 1
    if user_ticket[1] == pick_6[1]:
        count += 1
    if user_ticket[2] == pick_6[2]:
        count += 1
    if user_ticket[3] == pick_6[3]:
        count += 1
    if user_ticket[4] == pick_6[4]:
        count += 1
    if user_ticket[5] == pick_6[5]:
        count += 1
    return count

def payout(match):
    if match == 1:
        payout = 4
    elif match == 2:
        payout = 7
    elif match == 3:
        payout = 100
    elif match == 4:
        payout =50000
    elif match == 5:
        payout = 1000000
    elif match == 6:
        payout = 25000000
    else:
        payout = 0
    return payout

match = comp_tickets(user, winning)

print(payout(match))


balance = 0
times = 100000


for attempts in range(times):
    balance = balance - 2
    count = comp_tickets('user_ticket', 'pick_6')
    winnings = payout('match')
    #tot_win = balance / winnings

print(f"""
You played {times} times and spent {balance} dollars.
Your total winnings were {winnings} dollars.
""")