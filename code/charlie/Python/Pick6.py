import random

def pick6():
    temp = [random.randint(1, 100) for num in range(6)]
    temp.sort()
    return temp

def win_matches(win_nums, my_ticket, winnings):
    num_matches = 0
    for i in range(6):
        if win_nums[i] == my_ticket[i]:
            num_matches += 1
    
    if num_matches in winnings:
        return winnings[num_matches]

    return 0

def main():
    winnings = {6: 25000000, 5: 1000000, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}
    win_nums = pick6()
    my_ticket = pick6()
    balance = 0
    earnings = 0
    expenses = 0

    for i in range(100000):
        earnings += win_matches(win_nums, my_ticket, winnings)
        balance -= 2
        expenses += 2
        win_nums = pick6()
        my_ticket = pick6()

    ROI = (earnings - expenses)/expenses
    balance += earnings
    print("Earnings = ", earnings)
    print(f'Your balance after 100,000 plays = {balance}')
    print('Your ROI for this round = ', ROI)
main()