'''
=-=-= Lab14 28 Jan 2021 =-=-=
=-=-=-=-=- Pick 6 =-=-=-=-=-=
=-=-=- Composer: brndn -=-=-=
'''

import random    #imports random module

loop = 0         #loop flag
earnings = 0     #beginning earnings
expense = 0      #beginning expenses
winning = []     #winning numbers

win = {          #payouts per number of matching numbers
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
}

for i in range(6):
    winning.append(random.randint(1,99))

while loop < 100000:
    
    ticket = []    #numbers per ticket go here
    match = 0

    for i in range(6):                            #generates 6 random numbers 1-99
        ticket.append(random.randint(1, 99))    #adds them to the ticket numbers list
    
    for i in range(6):                 #compares the numbers in the tickets by index
        if winning[i] == ticket[i]:    #count matching indices
            match += 1

    earnings += win[match]   #gets winnings by matches from win dict -2 for ticket purchase
    expense += 2            #cost per ticket

    loop += 1    #advances the loop counter per loop

print(f'\nEarnings: ${earnings}')
print(f'\nExpense: ${expense}')
print(f'\nBalance: ${earnings - expense}')
print(f'\nROI: ${(earnings - expense) / expense}\n')