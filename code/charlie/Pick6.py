import random

def pick6():
    temp = [random.randint(1, 100) for num in range(6)]
    temp.sort()
    return temp

def win_matches(win_nums, my_ticket):
    num_matches = 0
    for i in range(6):
        if win_nums[i] == my_ticket[i]:
            num_matches += 1

    if num_matches == 1:
        return 4
    if num_matches == 2:
        return 7
    if num_matches == 3:
        return 100
    if num_matches == 4:
        return 50000
    if num_matches == 5:
        return 1000000
    if num_matches == 6:
        return 25000000

    return 0

def main():
    win_nums = pick6()
    my_ticket = pick6()
    balance = 0
    wins = 0
    i = 0

    while i < 100000:
        wins += win_matches(win_nums, my_ticket)
        balance -= 2
        i += 1
        win_nums = pick6()
        my_ticket = pick6()

    print(f'wins == {wins}')
    balance += wins 
    print(f'Your balance after 100,000 plays = {balance}')

main()