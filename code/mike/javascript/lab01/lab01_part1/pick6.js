/*
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
cost = 0
win = 0

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
    cost += 2 # increase total cost of $2 per ticket
    balance -= 2 # reduce $2 per ticket from balance
    win += pays[matching_nums] # calculate winnings from matches
    balance += pays[matching_nums] # adds winnings to balance

print(f'Balance: ${balance}') # Final Balance
print(f'ROI: ${(win-cost)/cost:.2f} ') # RIO
*/

let pays = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

let balance = 0
let cost = 0
let win = 0

function pick6() {
    ticket = []
    for (let num = 0; num <= 1; num++) {
        num = Math.floor(Math.random() * 99) + 1
        ticket.push(num)
    }
    return ticket
}

function num_matches(winning, ticket) {
    matching_nums = 0
    for (let x = 0; x <= winning.length; ++x) {
        if (winning[x] === ticket[x]) {
            matching_nums++
        }
    }
    return matching_nums
}

let winning_nums = pick6()

for (let x = 0; x <= 100000; x++) {
    ticket_nums = pick6()
    matching_nums = num_matches(winning_nums, ticket_nums)
    cost += 2
    balance -= 2
    win += pays[matching_nums]
    balance += pays[matching_nums]
}

let ROI = (win - cost) / (cost)
let newROI = ROI.toFixed(2)

alert(`Balance: $${balance}
ROI: $${newROI}`)