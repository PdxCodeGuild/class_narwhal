
/*
# Lab 15: Number to Phrase
# Richard
# January 28th, 2021

'''
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

```python
x = 67
tens_digit = x//10
ones_digit = x%10
```
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.
'''
*/


// define the variables that I will use and reference later


// 1. Ask the user for a number between 0 and 99
let input_number = parseInt(prompt("Enter a number between 0 and 99 inclusive: "))
//alert(input_number)

// 2. Convert the number as a digit to a word using a function

function convert_num_to_eng(number) {

    number = parseInt(number)
    let tens_digit
    let ones_digit
    let word1
    let word2 
    let result

    // reduce the number to less than 100 (if needed)
    number = number % 100


    tens_digit = Math.floor(number / 10)
    //console.log(tens_digit)

    ones_digit = number % 10
    //console.log(ones_digit)

    console.log("original number: " + number + " tens digit: " + tens_digit + " ones digit: " + ones_digit)

    if (number >= 10 && number <= 19) {
        if (number == 10) {
            result = "ten"
        }
        else if (number == 11) {
            result = "eleven"
        }
            
        else if (number == 12) {
            result = "twelve"
        }
        else if (number == 13) {
            result = "thirteen"
        }
        else if (number == 14) {
            result = "fourteen"
        }
        else if (number == 15) {
            result = "fifteen"
        }
        else if (number == 16) {
            result = "sixteen"
        }
        else if (number == 17) {
            result = "seventeen"
        }
        else if (number == 18) {
            result = "eighteen"
        }
        else if (number == 19) {
            result = "nineteen"
        }
    }

    if (number > 19) {
        if (tens_digit == 9) {
            word1 = "ninety-"
        }
        else if (tens_digit == 8) {
            word1 = "eighty-"
        }
        else if (tens_digit == 7) {
                word1 = "seventy-"
            }
        else if (tens_digit == 6) {
                word1 = "sixty-"
            }
        else if (tens_digit == 5) {
                word1 = "fifty-"
            }
        else if (tens_digit == 4) {
            word1 = "fourty-"
        }
        else if (tens_digit == 3) {
            word1 = "thirty-"
        }
        else if (tens_digit == 2) {
            word1 = "twenty-"
        }
        else {
            word1 = ""
        }
    }

    if (ones_digit == 9) {
        word2 = "nine"
    }
    else if (ones_digit == 8) {
        word2 = "eight"
    }
    else if (ones_digit == 7) {
        word2 = "seven"
    }
    else if (ones_digit == 6) {
        word2 = "six"
    }
    else if (ones_digit == 5) {
        word2 = "five"
    }
    else if (ones_digit == 4) {
        word2 = "four"
    }
    else if (ones_digit == 3) {
        word2 = "three"
    }
    else if (ones_digit == 2) {
        word2 = "two"
    }
    else if (ones_digit == 1) {
        word2 = "one"
    }
    else {
        word2 = ""
    }


    if (number >=20 ) {
        result = word1 + word2
    }
    else if (number < 10) {
        result = word2
    }
    else {
        result = result
    }

    if (number == 0) {
        result = "zero"
    }
 
return result
}


// apply the function to the input
let output = convert_num_to_eng(input_number)

//display output as popup
alert(output)





/*
'''
## Version 2

Handle numbers from 100-999.
'''

def hundreds(number):
    hundreds_digit = number // 100
    # print(hundreds_digit)
    if hundreds_digit == 9:
        word = "nine-hundred-"
    elif hundreds_digit == 8:
        word = "eight-hundred-"
    elif hundreds_digit == 7:
        word = "seven-hundred-"
    elif hundreds_digit == 6:
        word = "six-hundred-"
    elif hundreds_digit == 5:
        word = "five-hundred-"
    elif hundreds_digit == 4:
        word = "four-hundred-"
    elif hundreds_digit == 3:
        word = "three-hundred-"
    elif hundreds_digit == 2:
        word = "two-hundred-"
    elif hundreds_digit == 1:
        word = "one-hundred-"
    else:
        word = ""
    return(word)
'''
'''
# print(hundreds(151))
# print(hundreds(444))
# print(hundreds(999))
'''
'''

def final(number):
    first_part = hundreds(number)
    last_part = convert_num_to_eng(number)
    if number % 100 == 0:
        last_part = ""

    if number == 0:
        result = "zero"
    
    else:
        result = first_part + last_part

    # remove the trailing slash if there is one
    if result.endswith("-"):
        result = result[:-1]

    return(result)


print(final(0))
print(final(17))
print(final(89))
print(final(100))
print(final(200))
print(final(167))
print(final(190))
print(final(444))
print(final(999))

*/
