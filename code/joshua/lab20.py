'''
Josh Novac
Lab 20
Python
PDX Code Guild
'''


# defined function to validate credit card number
def validate():
    numbers = [int(i) for i in card_number]
    sliced_number = numbers.pop()
    reversed_numbers = list(reversed(numbers))
    numbers[::2] = [i*2 for i in numbers[::2]]
    numbers = [i-9 if i > 9 else i for i in numbers]
    numbers = sum(numbers) % 10
    if numbers == sliced_number:
        return 'Valid'
    if numbers != sliced_number:
        return 'Not Valid'
# asking input from user
card_number = input('Enter card number: ')
# prints the result
print(validate())


''' STEP-BY-STEP 

write a function which returns whether a string containing a credit card number is valid as a boolean.

# 1. Convert the input string into a list of ints.
## numbers = [int(i) for i in card_number]

# 2. Slice off the last digit. That is the check digit.
## sliced_number = numbers.pop()

# 3. Reverse the digits.
## reversed_numbers = list(reversed(numbers))

# 4. Double every other element in the reversed list.
## numbers[::2] = [i*2 for i in numbers[::2]]

# 5. Subtract nine from numbers over nine.
## numbers = [i-9 if i > 9 else i for i in numbers]

# 6. Sum all values.
## 85
# for example, card number '4556737586899855', it would be a sum of 85

# 7. Take the second digit of that sum.
## numbers = sum(numbers) % 10 ---> 5

# If that matches the check digit, the whole card number is valid.
## 5 == 5; True ---> Valid
## 5 != 5; False ---> Not Valid

'''