'''
----------------
Josh Novac
Lab 13
Python
PDX Code Guild
----------------
'''

'''
/////////////////////////////////////////////////////////////////////////////////
DEFINED FUNCTIONS
/////////////////////////////////////////////////////////////////////////////////
'''
# defined function to encrypt letters and add spaces between words
def encrypt(message, shift):
    encrypt = ''
    for letter in message:
        if letter != ' ':
            num = (english[letter] + shift) % 26
            encrypt += rot13[num]
        else:
            encrypt += ' '

    return encrypt

# defined function to decrypt letters and add spaces between words
def decrypt(message, shift):
    decrypt = ''
    for letter in message:
        if letter != ' ':
            num = (english[letter] - shift + 26) % 26
            decrypt += rot13[num]
        else:
            decrypt += ' '

    return decrypt

# defined function to be able to run cipher/decipher program as a whole
def cipher():
    
    message = input('\nEnter Message To Encrypt>>: ')
    shift = 13
    result = encrypt(message.upper(), shift)
    print(f'\nEnglish = {message.upper()} \nROT13 = {result}')

    print('\n---------------------------------------------------------')
    print('Enter your ROT13 message to decrypt it back into English'.upper())
    print('---------------------------------------------------------\n')

    message = input('Enter Message To Decrypt>>: ')
    shift = -13
    result = decrypt(message.upper(), shift)
    print(f'\nEnglish = {message} \nROT13 = {result}\n')


'''
//////////////////////////////////////////////////////////////////////////////////////////////////
DICTIONARIES
//////////////////////////////////////////////////////////////////////////////////////////////////
'''

# dictionary for English characters
english = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}
# dictionary for ROT13 setup
rot13 = {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
    22: 'V', 23: 'W', 24: 'X', 25: 'Y'
    }


'''
/////////////////////////////////////////////////////////////////////////////////////////////////////////
RUN PROGRAM FUNCTION
////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
# calling the defined function cipher() to run program
cipher()