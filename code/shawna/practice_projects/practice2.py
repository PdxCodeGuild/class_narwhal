# Practice: Strings
# For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

# Get a string from the user, print out another string, doubling every letter.
def practice_one():
    str = input("Write out a sentence here:  ")
    output = "".join([2*l for l in str])
    return (output)

# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.

def practice_two():
    word = input("Gimme a word:  ")
    missing_ltr = [word.replace(i, "", 1) for i in word ]
    return (missing_ltr)

# Problem 3
# Return the letter that appears the latest in the english alphabet.

def practice_three():
    word = input("Gimme a long word and I will tell you which letter appears last ing the alphabet:  ")
    ltr = sorted((list(word)))[-1]
    return (ltr)

# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.
def practice_four():
    phrase = input("Write the string in which you would like to count the substring here:  ")
    substring = input("Write the substring that you would like me to track here:  ")
    
    return phrase.count(substring)

# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
def practice_five():
    string = input("Type out some 'cat's and some 'dog's here and I will tell you if they are even.  ")
    substring1 = "cat"
    substring2 = "dog"
    return string.count(substring1) == string.count(substring2)

print(practice_five())
# Problem 6
# Return the number of letter occurances in a string.

# def count_letter(letter, word):
#     ...
# count_letter('i', 'antidisestablishmentterianism') → 5
# count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2
# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.

# lower_case("SUPER!") → 'super!'
# lower_case("        NANNANANANA BATMAN        ") → 'nannananana batman'