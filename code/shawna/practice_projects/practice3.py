# Problem 1 Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
import random

fruits = ['apples', 'bananas', 'pears']

def random_element(a):
    x = random.randint(0,3)
    return a[x]

print(random_element(fruits))