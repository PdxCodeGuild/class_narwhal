from random import randint


winnners_dict = {1:"$4",
                2:"$7",
                3:"$100",
                4:"$50,000",
                5:"$1,000,000",
                6:"$25,000,000"}


def pick_6():
    numbers = []
    while len(numbers) < 6:
        num = randint(1,99)
        if num not in numbers:
            numbers.append(num)
    return numbers


winning_ticket = pick_6()



for i in range (10):
    random_ticket = pick_6()
    print(random_ticket)


balance = 0
earnings = 0
expenses = 0


#while loop < 100000: 


print(pick_6())


             
