'''
Lab 15
Version 2
Numbers to Phrase
'''

# Dictionary converting the hundreds digit
convert_huns = {
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
    0 : '',
    1 : 'ten',
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

def pull_huns(h):
    huns = dig//100
    convert_huns.get(huns)
    return (h[huns])


def pull_teens(te):
    teens = dig%10
    convert_teens.get(teens)
    return (te[teens])

def pull_tens(t):
    if dig > 99:
        tens = dig%100//10
        return convert_tens.get(tens)
    else:
        tens = dig//10
        convert_tens.get(tens)
        return (t[tens])


def pull_ones(o):
    ones = dig%10
    dash = '-'
    if ones == 0:
        return ''
    elif dig > 10 and dig < 99:
        convert_ones.get(ones)
        return dash + (o[ones])
    elif dig > 110 and dig < 999:
        convert_ones.get(ones)
        return dash + (o[ones])
    else:
        convert_ones.get(ones)
        return (o[ones])

dig = int(input('Enter a number between 0 and 999: '))

if dig == 100:
    print(f'{pull_huns(convert_huns)} hundred {pull_tens(convert_tens)}{pull_ones(convert_ones)}')
elif dig > 109 and dig < 120:
    print(f'{pull_huns(convert_huns)}-hundred {pull_teens(convert_teens)}')
if dig > 100 and dig < 1000:
    print(f'{pull_huns(convert_huns)}-hundred {pull_tens(convert_tens)}{pull_ones(convert_ones)}')
elif dig > 19 and dig < 100:
    print(f'{pull_tens(convert_tens)}{pull_ones(convert_ones)}')
elif dig > 9 and dig < 20:
    print(pull_teens(convert_teens))
elif dig > 0 and dig < 10:
    print(pull_ones(convert_ones))
elif dig == 0:
    print('zero')
else:
    print('You did not enter a valid number!')

