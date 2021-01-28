# ---- Practice Strings ---- #

# - Problem 1 - #

# Get a string from the user, print out another string, doubling every letter. #

def double_letters(x):
    new_string = ""
    for letter in x:
        new_string = new_string + letter
        new_string = new_string + letter
    return new_string

x = input('Enter a word: ')

print(double_letters(x))

# - Problem 2 - #

# Write a function that takes a string, and returns a list of strings, each missing a different character. #

# this doens't work for some reason #

def missing_char(word):
    result = []
    for char in word:
        newword = word
        result.append(newword.replace(char,""))
    return result

word = input('Enter a word: ')
print(missing_char(word))