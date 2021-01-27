user_input = input("Please enter a whole number between 0 and 999:  ")
number = int(user_input)

hundreds_digit = (number // 100)
tens_digit = (((number - (hundreds_digit * 100)) // 10) * 10)
ones_digit = (number % 10)

def number_to_word(value):
    value = str(value)
    numbers_to_words = {
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
        "20": "twenty ",
        "30": "thirty ",
        "40": "fourty ",
        "50": "fifty ",
        "60": "sixty ",
        "70": "seventy ",
        "80": "eighty ",
        "90": "ninety ",
    }
    return (numbers_to_words.get(value))

def words(ones, tens="0", hundreds="0"): 
        tens_word = number_to_word(tens)
        hundreds_word = ""
        ones_word = number_to_word(ones)

        if hundreds != 0:
            hundreds_word = (number_to_word(hundreds) + 'hundred ')

        statement = (f"{hundreds_word}{tens_word}{ones_word}").strip()

        return statement.capitalize()

print(words(ones_digit, tens_digit, hundreds_digit))