'''
Lab 13
Version 2
ROT Cipher
'''
import string

abc = string.ascii_lowercase
ABC = string.ascii_uppercase
output = ''

# User inputs letter code to be encrypted or decrypted
user_input = input('Enter your code to be decrypted (a-z): ')
rotations = int(input('How many rotations would you like?: '))

# determines case of letter, adds 13 then modulo 26
for letter in user_input:
    if letter in abc:
        output += abc[(abc.index(letter) + rotations) % 26]
    elif letter in ABC:
        output += ABC[(ABC.index(letter) + rotations) % 26]
    else:
        output += letter


print(f'User input: {user_input}')
print(f'Number of rotations: {rotations}')
print(f'Output code: {output}')