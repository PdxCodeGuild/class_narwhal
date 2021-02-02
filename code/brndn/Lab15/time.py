'''
=-=-= Lab15 V4 01 Feb 2021 =-=-=
=-=-=-=- Time to phrase -=-=-=-=
=-=-=-= Composer: brndn -=-=-=-=
'''

hours = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
}

minute_ones = {
    0: "",
    1: "-one",
    2: "-two",
    3: "-three",
    4: "-four",
    5: "-five",
    6: "-six",
    7: "-seven",
    8: "-eight",
    9: "-nine",
}

minute_teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

minute_tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
}

while True:
    try:
        time = input("\nWhat's the time?: ").split(":")
        hour = hours[time[0]]
        min_ten = int(time[1])//10
        min_one = int(time[1])%10
        if min_ten == 1:
            minute = ' ' + minute_teens[min_ten*10 + min_one]
        elif min_ten == 0 and min_one == 0:
            minute = "-o-clock"
        elif min_ten == 0 and min_one != 0:
            minute = f'-o{minute_ones[min_one]}'
        else:
            minute = ' ' + minute_tens[min_ten] + minute_ones[min_one]
        break
    except:
        print('\nPlease use HOUR:MINUTE format.')
    
print(f'\nIt\'s {hour}{minute}\n')