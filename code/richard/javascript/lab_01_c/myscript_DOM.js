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

function convert_num_to_eng() {


// 1. Ask the user for a number between 0 and 99
let number
number = document.getElementById("number_input").value
console.log('input number: ' + number)
// alert(number)

// 2. Convert the number as a digit to a word using a function



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

    console.log("original number: " + number);
    console.log(" tens digit: " + tens_digit);
    console.log(" ones digit: " + ones_digit);

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
 
// return result



// apply the function to the input
//let output = convert_num_to_eng(number)

//display output on the screen
document.getElementById("word_output").innerHTML = result;

}




// Recalculate when someone clicks the button

// when someone uses the mouse
calcBtn.addEventListener('click', convert_num_to_eng)

// when someone uses the keyboard
calcBtn.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        convert_num_to_eng()
    }
})




