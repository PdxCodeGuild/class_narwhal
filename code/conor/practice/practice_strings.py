# ---- Practice Strings ---- #

# - Problem 1 - #

# Get a string from the user, print out another string, doubling every letter. #
'''
def double_letters(x):
    new_string = ""
    for letter in x:
        new_string = new_string + letter
        new_string = new_string + letter
    return new_string

x = input('Enter a word: ')

print(double_letters(x))
'''
# - Problem 2 - #

# Write a function that takes a string, and returns a list of strings, each missing a different character. #
'''
def missing_char(word):
    result = []
    for char in word:
        newword = word
        result.append(newword.replace(char,""))
    return result

word = input('Enter a word: ')
print(missing_char(word))s
'''
# - Problem 3 - #

# Return the letter that appears the latest in the English Alphabet #
'''
word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
word_1 = sorted(word)
latest_letter = word_1[-1]
print(f"""
In the word {word},
the last letter occuring in the english alphabet is '{latest_letter.upper()}'.
""")
'''
# - Problem 4 - #

# write a function that returns the number of occurances of 'hi' in a given string. #
'''
def count_hi(word):
    return word.count('hi')

count_hi = count_hi('hihi')
print(f'The word "hi" occurs {count_hi} times in the word "hihi".')
'''
# - Problem 5 - #

# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

