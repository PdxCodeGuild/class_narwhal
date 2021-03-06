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

#print(even_count((1, 2, 3, 4)))
#print(even_count((1, 2, 3)))

#Problem 4 Print out every other element of a list, first using a while loop, then using a for loop.

def while_even():
    l = ("apples", "bananas", "carrots", "dragonfruit", "escrole", "figs", "grapefruit")
    i = 0
    output = []
    while (i < len(l)):
        if ((i == 0) or (i % 2 == 0)):
            output.append(l[i])
        i += 1
    return output      

#print(while_even())

def for_even():
    l = ("apples", "bananas", "carrots", "dragonfruit", "escrole", "figs", "grapefruit")
    output = []
    for count, word in enumerate(l):
        if (count == 0) or(count %2 == 0):
            output.append(word)
    return output

#print(for_even())

# Problem 5 Write a function that returns the reverse of a list.
def reverse_list():
    l = ["apples", "bananas", "carrots", "dragonfruit", "escrole", "figs", "grapefruit"]
    output = []

    for word in range ((len(l) -1), -1, -1):
        output.append((l[word]))
    return output   
        
#print(reverse_list())


#Problem 6 #Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def less_ten(nums):
    output = [num for num in nums if num < 10]
    return output

#print(less_ten([1, 19, 22, 10, 4, 3, 28, 2, -1]))

#Problem 7 Write a function to find all common elements between two lists.
def common_elements(l1, l2):
    set1 = set(l1)
    set2 = set(l2)

    if (set1 & set2):
        return (set1 & set2)
    else:
        return ("No matching elements")
    

#print(common_elements(["apples", "bananas", "carrots", "dragonfruit", "escrole", "figs", "grapefruit"], ["monkeys", "eat", "many", "bananas"]))

#Problem 8 Write a function to combine two lists of equal length into one, alternating elements.

def combine(l1, l2):
    output = []
    for i in range(len(l1)):
        output.append(l1[i])
        output.append(l2[i])
    return output

#print(combine(['a','b','c'],[1,2,3]))

#Problem 9 Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
def find_pair(nums, target):
    pair = []
    for num1 in nums:
        value = (target - num1)
        for num2 in nums:
            if (num2 == value):
                pair.append(num2)
    return pair


print(find_pair([5, 6, 2, 3], 7))
