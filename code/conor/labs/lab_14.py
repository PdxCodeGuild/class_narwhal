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

def comp_tickets(user, winning):
    count = 0
    if user == winning:
        count += 1
    if user[0] == winning[0]:
        count += 1
    if user[1] == winning[1]:
        count += 1
    if user[2] == winning[2]:
        count += 1
    if user[3] == winning[3]:
        count += 1
    if user[4] == winning[4]:
        count += 1
    if user[5] == winning[5]:
        count += 1
    return count

match = comp_tickets(user, winning)
print(match)

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

pay = payout(match)

print(payout(match))


balance = 0
times = 100000
count = 0
matches = 0
winnings = 0

for attempts in range(times):
    balance = balance - 2
    winning = pick_6()
    user = user_ticket()
    match = comp_tickets(user, winning)
    pay = payout(match)
    winnings = pay
    
return_on_invest = balance + winnings
    

print(f"""
You played {times} times and spent {balance} dollars.
Your total winnings were {winnings} dollars.
Your Return on Investment was {return_on_invest} dollars.
""")