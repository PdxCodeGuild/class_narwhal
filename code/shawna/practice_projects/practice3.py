# Problem 1 Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
import random

fruits = ['apples', 'bananas', 'pears']

def random_element(a):
    x = random.randint(0,3)
    return a[x]

#print(random_element(fruits))

#Problem 2 Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
def number_loop():
    output = []
    while True:
        num = input("Enter a number or enter 'done' when complete:  ")
        if num.lower() == "done":
            return (output)
            break
        else:
            num = int(num)
            output.append(num)
#print(number_loop())

#Problem 3 Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_count(numbers):
    return len(numbers) %2 == 0

print(even_count((1, 2, 3, 4)))
print(even_count((1, 2, 3)))
