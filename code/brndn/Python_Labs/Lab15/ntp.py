'''
=-=-= Lab15 28 Jan 2021 =-=-=
=-=-=- Number to Phrase =-=-=
=-=-=-= Composer: brndn =-=-=
'''

#dictionaries of number to word conversions
ones = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

teens = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}

tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

def num_sort(first, second = "", third = ""):    #function to sort number and retrieve words from dictionaries
    if second == "":
        word = ones[first]
    elif first == "1" and third == "":
        word = teens[first + second]
    elif second == "0" and third == "":
        word = tens[first]
    elif third == "":
        word = tens[first] + "-" + ones[second]
    elif second == "0" and third != "0":
        word = f"{ones[first]} hundred {ones[third]}"
    elif second == "0" and third == "0":
        word = ones[first] + " hundred"
    elif second == "1":
        word = f"{ones[first]} hundred {teens[second + third]}"
    else:
        word = f"{ones[first]} hundred {tens[second]}-{ones[third]}"
    return word

num = input("\n>>> ")    #input number 0 - 999

nums = list(num)    #input number separated into a list

if len(nums) == 1:             #determine length of list
    ans = num_sort(nums[0])    #to pass digits into appropriate parameter of function

elif len(nums) == 2:
    ans = num_sort(nums[0], nums[1])

elif len(nums) == 3:
    ans = num_sort(nums[0], nums[1], nums[2])

print(f"\n{ans}\n")