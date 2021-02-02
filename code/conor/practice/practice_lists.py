# ---- Practice Lists ---- #

# - Problem 1 - #

# Write a function using random.randint to generate and index to pick a random element of a list and return it. #
'''
import random

def random_element(fruits):
    rand = random.randint(0, 2)
    return fruits[rand]

fruits = ['apples', 'bananas', 'pears']

print(f'Your random fruit is: {random_element(fruits)}')
'''
# - Problem 2 - #

# Write a REPL which asks users for a list of numbers, which are enterd until they day done. Print out the list. #
'''
output = []

while True:
    number = input('Enter a number or say "done": ')
    if number == 'done':
        print(f"Your numbers are: {output}")
        break
    else:
        number = int(number)
        output.append(number)
'''
# - Problem 3 - #

# Write a function that takes a list of numbers and returns true if there is an even number of even numbers #
