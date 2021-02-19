# Lab 20: Credit Card Validation
# Richard
# January 28th, 2021
'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. 
The steps are as follows:

1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.
'''
# Made up credit card numbers
credit_card_test = "4556737586899855" # original credit card number given to test
# credit_card_test = "4111111111111111"
# credit_card_test = "5500000000000004"

'''
Sample credit card numbers from https://www.easy400.net/js2/regexp/ccnums.html
Visa 	4111 1111 1111 1111 
MasterCard 	5500 0000 0000 0004 
American Express 	3400 0000 0000 009 
Diner's Club 	3000 0000 0000 04 
Carte Blanche 	3000 0000 0000 04 
Discover 	6011 0000 0000 0004 
en Route 	2014 0000 0000 009 
JCB 	3088 0000 0000 0009
'''

# 1. Convert the string into a list of intergers
# 1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
cc_list = [(x) for x in credit_card_test]
cc_list = list(map(int, cc_list)) 
print(f"List of integers: {cc_list}")

# save the check digit to compare later
check_digit = cc_list[-1]
print(f"check digit: {check_digit}")

# 2. Slice off the last Digit
# 2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
cc_list = cc_list[:-1]
print(f"Last digit sliced off: {cc_list}")

# 3. Reverse the digits
# 3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
cc_list.reverse()
print(f"Digits Reversed: {cc_list}")


# 4. Double every other element in the reversed list.
# 4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
l = cc_list[:]
l[::2] = [x*2 for x in l[::2]]
print(f"Every other element doubled: {l}")


# 5. Subtract nine from numbers over nine.
# 5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
l2 = []
for item in l:
    if item > 9:
        item = item - 9
    l2.append(item)
print(f"subtract 9 from numbers over 9: {l2}")


# 6. Sum all values.
# 6. 85
total = sum(l2)
print(f"total: {total}")

# 7. Take the second digit of that sum.
# 7. 5
number_sum = str(total)
second_digit = number_sum[1:2]
print(f"second digit: {second_digit}")

# 8. If that matches the check digit, the whole card number is valid.
# 8. Valid!
if int(second_digit) == check_digit:
    print("Valid!")
else:
    print("Not Valid")

