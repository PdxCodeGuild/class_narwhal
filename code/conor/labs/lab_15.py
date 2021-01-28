# ---- Lab 15 ---- #

# - Convert Numbers to Phrase - #

ones_dict = {
    0 : 'Zero',
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    10 : 'Ten',
    11 : 'Eleven',
    12 : 'Twelve',
    13 : 'Thirteen',
    14 : 'Fourteen',
    15 : 'Fifteen',
    16 : 'Sixteen',
    17 : 'Seventeen',
    18 : 'Eighteen',
    19 : 'Nineteen',
}

tens_dict = {
    2 : 'Twenty',
    3 : 'Thirty',
    4 : 'Fourty',
    5 : 'Fifty',
    6 : 'Sixty',
    7 : 'Seventy',
    8 : 'Eighty',
    9 : 'Ninety'
}

num = int(input('Enter a number 0-999: '))

hundreds = num // 100
tens = num // 10 % 10
ones = num % 10

def num_to_word(num):
    if 0 <= num <= 19:
        return ones_dict[num]
    elif 20 <= num <= 99:
        num_2 = tens_dict[tens] + '-' + ones_dict[ones]
        return num_2
    elif 100 <= num <= 999:
        num_3 = ones_dict[hundreds] + '-' + 'Hundred' + ' and ' + tens_dict[tens] + '-' + ones_dict[ones]
        return num_3

print(num_to_word(num))


