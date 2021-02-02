# ---- Lab 13 ---- #

# - ROT13 - #

import string

# import the alphabet
alpha = string.ascii_lowercase

# get in input phrase, make it lower case and turn it into a list
phrase = input('Enter a phrase: ').lower()
phrase = list(phrase)

# get the amount of encryption
encrypt = input('Enter the desired Encryption number: ')
encrypt = int(encrypt)

# output phrase is a blank string
output_phrase = ''

# find the letters, get the index. Add the letters to blank string
for i in phrase:
    if i in list(alpha):
        i = alpha.find(i) + encrypt
        output_phrase += alpha[i%26]
    else:
        output_phrase += i

# print output phrase
print(f'{output_phrase}')