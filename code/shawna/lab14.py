import random

def random_numbers():
    """Generate a list of 6 random numbersb"""
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 69)
        if num not in numbers:
             numbers.append(num)
    return(numbers)

def compare(ticket_numbers, winning_numbers):
    count = 0
    for i, num in enumerate(ticket_numbers):
       if num == winning_numbers[i]:
            count += 1
    return(count)

winnings = {
    "0" : 0,
    "1" : 4,
    "2" : 7,
    "3" : 100,
    "4" : 50000,
    "5" : 1000000,
    "6" : 25000000
}

wallet = 0
number_of_tickets = 100000
winning_numbers = random_numbers()

for i in range(number_of_tickets):
    ticket = random_numbers()
    wallet -= 2
    winning_number_count = compare(ticket, winning_numbers)
    prize_money = winnings.get(str(winning_number_count))
    wallet += int(prize_money)


print(wallet)

