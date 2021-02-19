'''
Lab 15
Version 1
Numbers to Phrase
'''

# Dictionary converting the teens digit
convert_teens = {
    0 : 'ten',
    1 : 'eleven',
    2 : 'twelve',
    3 : 'thirteen',
    4 : 'forteen',
    5 : 'fifteen',
    6 : 'sixteen',
    7 : 'seventeen',
    8 : 'eighteen',
    9 : 'nineteen'
    }

# Dictionary converting the tens digit
convert_tens = {
    '': '',
    1 : 'teen',
    2 : 'twenty',
    3 : 'thirty',
    4 : 'forty',
    5 : 'fifty',
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    9 : 'ninety'
    }

# Dictionary converting the ones digit
convert_ones = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    }


def pull_teens(te):
    teens = dig%10
    convert_teens.get(teens)
    return (te[teens])

def pull_tens(t):
    tens = dig//10
    convert_tens.get(tens)
    return (t[tens])


def pull_ones(o):
    tens = dig//10
    ones = dig%10
    dash = '-'
    if ones == 0:
        return ''
    elif tens == 0:
        convert_ones.get(ones)
        return (o[ones])
    else:
        convert_ones.get(ones)
        return dash + (o[ones])

dig = int(input('Enter a number between 0 and 99: '))

if dig > 19 and dig < 100:
    print(f'{pull_tens(convert_tens)}{pull_ones(convert_ones)}')
elif dig > 9 and dig < 20:
    print(pull_teens(convert_teens))
elif dig > 0 and dig < 10:
    print(pull_ones(convert_ones))
elif dig == 0:
    print('zero')
else:
    print('You did not enter a valid number!')
