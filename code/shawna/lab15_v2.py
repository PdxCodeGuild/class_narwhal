user_input = input("Please enter a whole number between 0 and 999:  ").strip(",")
number = list(reversed(list(user_input)))


words = {
        "0": "",
        "1": "one ",
        "2": "two ",
        "3": "three ",
        "4": "four ",
        "5": "five ",
        "6": "six ",
        "7": "seven ",
        "8": "eight ",
        "9": "nine ",
        "10": "ten ",
        "11": "eleven ",
        "12": "twelve ",
        "13": "thirteen ",
        "14": "fourteen ",
        "15": "fifteen ",
        "16": "sixteen ",
        "17": "seventeen ",
        "18": "eighteen ",
        "19": "nineteen ",
        "20": "twenty ",
        "30": "thirty ",
        "40": "fourty ",
        "50": "fifty ",
        "60": "sixty ",
        "70": "seventy ",
        "80": "eighty ",
        "90": "ninety ",
}

positions = {
    "0": "one",
    "1": "ten",
    "2": "hundred",
    "3": "thousand",
    "4": "ten_thousand",
    "5": "hundred_thousand",
    "6": "million",
    "7": "ten_million",
    "8": "hundred_million",
    "9": "billion",
}

def convert(number):
    """ Converts number value to string. Returns list of words."""

    converted = []
    for n in range(len(number)):
        word = ""
        # tens, ten thousands, ten millions place logic
        if n == 1 or n == 4 or n == 7:
            #checks if the tens place is a one
            if number[n] == "1":
                #returns the value of 10 + ones place 
                value = (int(number[n - 1]) + 10)
                #gets word for the "teen" number
                word = words.get(str(value))
            else:
                #multiplys number by ten to get the full tens place (i.e. 20, 30, 40)
                #let's the ones handle itself
                value = ((int(number[n])) * 10)
                #gets tens word from dictionary
                word = words.get(str(value))
        #hundreds        
        elif n == 2 or n == 5 or n == 8:
            word = (words.get(number[n]) + "hundred ")
        #thousands
        elif n == 3:
            if  ((n + 1) < len(number)) and number[n + 1] == "1":
                    word = "thousand "
            else:
                word = (words.get(number[n]) + "thousand ")
        #millions
        elif n == 6:
            if ((n + 1) < len(number)) and number[n + 1] == "1":
                word = "million "
            else:
                word = (words.get(number[n]) + "million ")
        #billions
        elif n == 9:
            if number[5] == "1":
                word = "billion "
            else:
             word = words.get(number[n] + "billion ")
        #evaluates ones position, if tens position is 1 it will skip
        else:
            if number[n + 1] == "1":
                pass 
            else:
                word = words.get(number[n])
        
        converted.append(word)

    return(list(reversed(converted)))

print(convert(number))
str = ''.join(convert(number))

print(str.capitalize())
