# ---- Practice Strings ---- #

# - Problem 1 - #

def double_letters(x):
    new_string = ""
    for letter in x:
        new_string = new_string + letter
        new_string = new_string + letter
    return new_string

x = input('Enter a word: ')

print(double_letters(x))

# - Problem 2 - #

# in progress # 