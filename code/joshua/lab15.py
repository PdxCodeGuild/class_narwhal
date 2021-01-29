'''
Josh Novac
Lab 15
Python
PDX Code Guild
'''

'''
Version 1 -------------------------------------------------------------------------
'''

# defined function to covert numbers into words
def convert():
    if user_input == 0:
        print('zero')
    elif user_input >= 1 and user_input < 20:
        print(ones[user_input])
    elif user_input >= 20 and user_input <= 99:
        print(f'{tens[ten]} {ones[one]}')
    return


# list of numbers 1-19
ones = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'tweleve', 'thirteen', 'fourteen', 'fifteen', 
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]

# list of tens place    
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety'
    ]

#user's input - asks user to enter number from 0-99
user_input = int(input('Enter a number 0-99: '))

# conversion for each number place
one = user_input % 10
ten = user_input // 10

# defined function that runs the above code
convert()