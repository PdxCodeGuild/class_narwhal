# Problem 1 Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
import random

fruits = ['apples', 'bananas', 'pears']

def random_element(a):
    x = random.randint(0,3)
    return a[x]

#print(random_element(fruits))

def number_loop():
    output = []
    while True:
        num = input("Enter a number or enter 'done' when complete:  ")
        if num.lower() == "done":
            print(output)
            break
        else:
            num = int(num)
            output.append(num)
number_loop()