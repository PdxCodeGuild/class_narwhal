'''
Lab 13
Version 1
ROT Cipher
'''
import string

abc = string.ascii_lowercase
ABC = string.ascii_uppercase
output = ''

# User inputs letter code to be encrypted or decrypted
user_input = input('Enter your code to be decrypted (a-z): ')

# determines case of letter, adds 13 then modulo 26
for letter in user_input:
    if letter in abc:
        output += abc[(abc.index(letter) + 13) % 26]
    elif letter in ABC:
        output += ABC[(ABC.index(letter) + 13) % 26]
    else:
        output += letter


print(user_input)
print(output)