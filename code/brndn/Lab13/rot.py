'''
=-=-= Lab13 29 Jan 2021 =-=-=
=-=-=-=-= ROT Cipher -=-=-=-=
=-=-=- Composer: brndn -=-=-=
'''

import string

letters = string.ascii_lowercase

entry = input('\nEncode: ').lower()
try:
    amt = int(input('\nROT: '))      #ROT variable
except ValueError:                   #account for non-number entries
    amt = 13                         #default ROT variable

cipher = ''

for l in entry:                      #for each letter in the entered string
    if l not in letters:             #skip over characters not in alphabet
        continue                     
    index = letters.find(l) + amt    #find the letter in the alphabet (ascii_lowercase) and get rotated index
    while index > 25:                #for multiple index overages by 25
        if index > 25:               #if index > 25
            index -= 26              #subtract 26 to return to first index of alphabet
    cipher += letters[index]         #add the letter of rotated index to the encrypted string

print(f'\n"{cipher}"\n')