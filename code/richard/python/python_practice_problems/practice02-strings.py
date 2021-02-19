
# Practice: Strings

# For each practice problem, write a function that returns a value (not just prints it). 
# You can then call the function a couple # times to test it, comment those calls out, 
# and move on to the next problem. An example of this format is given below.
'''
```python
def add(a, b):
    return a + b
#print(add(5, 2))
#print(add(8, 1))
```
'''

## Problem 1

# Get a string from the user, print out another string, doubling every letter.


def double_letters(x):
    new_string = ""
    for letter in x:
        new_string = new_string + letter
        new_string = new_string + letter
    print(new_string)

    ...
double_letters('hello')
# hheelllloo


## Problem 2

# Write a function that takes a string, and returns a list of strings, each missing a different character.

def missing_char(word):
    result = []
    for char in word:
        new_word = word
        result.append(new_word.replace(char, ""))
    print(result)


missing_char('kitten') # → ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']


## Problem 3
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    a = word
    b = sorted(a)
    print("The latest letter is " + b[-1])
    

latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# the latest letter is v.


## Problem 4

# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(word):
    print(word.count("hi"))


count_hi('hihi') # → 2


## Problem 5

# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

def cat_dog(input):
    dog_count = input.count("dog")
    cat_count = input.count("cat")
    if dog_count == cat_count:
        return True
    else:
        return False

print(cat_dog('catdog')) # → True
print(cat_dog('catcat')) # → False
print(cat_dog('catdogcatdog')) # → True



## Problem 6

# Return the number of letter occurances in a string.

def count_letter(letter, word):
    count = 0
    for item in range(len(word)):
        if letter == word[item]:
            count += 1
    return count

    ...
print(count_letter('i', 'antidisestablishmentterianism')) # → 5
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # → 2


## Problem 7

# Convert input strings to lowercase without any surrounding whitespace.
def lower_case(stuff):
    stuff = stuff.strip()
    stuff = stuff.lower()
    return(stuff)

print(lower_case("SUPER!")) # → 'super!'
print(lower_case("        NANNANANANA BATMAN        ")) # → 'nannananana batman'
