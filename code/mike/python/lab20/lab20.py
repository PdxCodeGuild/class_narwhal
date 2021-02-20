'''
Lab 20
Credit Card Validation
'''

'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''
card_no = []
index = 0

user_num = input('Please enter your credit card number for validation: ')

#change to int in list
for x in user_num:
    card_no.append(int(x))

step_1 = card_no 

step_2 = step_1[0:-1:] # remove last digit

step_3 = step_2[::-1] # reverse list

step_4 = [x*2 if y%2 == 0 else x for y, x in enumerate(step_3)] # double every other number

step_5 = [x-9 if x>9 else x for x in step_4] # subtract 9 from numbers greater than 9

step_6 = sum(step_5) # add all numbers together

step_7 = step_6%10 # gets second number

# determines if value matches last digit on card
if step_7 == card_no.pop():
    step_8 = 'Valid!'
else:
    step_8 = 'Not a valid card number!'


print(f'1. {step_1}')
print(f'2. {step_2}')
print(f'3. {step_3}')
print(f'4. {step_4}')
print(f'5. {step_5}')
print(f'6. {step_6}')
print(f'7. {step_7}')
print(f'8. {step_8}')