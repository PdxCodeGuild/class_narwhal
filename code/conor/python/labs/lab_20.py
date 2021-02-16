# ---- Lab 13 ---- #

# - Credit Card Validation - #

# Given test card number #

card_num = input('Enter your card number: ')

# Turn the number into a list #
card_list = [(x) for x in card_num]
card_list = list(map(int, card_list))
print(card_list)

# Save the last number to check at the end #
check = card_list[-1]

# Remove the last number #
card_list = card_list[:-1]
print(card_list)

# Reverse the list #
card_list = card_list[::-1]
print(card_list)

# Double every other element in list #
card_list = [num * 2 if i % 2 == 0 else num for i, num in enumerate(card_list)]
print(card_list)

# Subtract 9 from numbers over 9 #   
card_list = [(num - 9) if num > 9 else num for num in card_list]
print(card_list)

# Sum of all values #
sum_card_list = sum(card_list)
print(sum_card_list)

# Take the second digit #
second_digit = sum_card_list % 10
print(second_digit)
print(check)
# Match the Second Digit with the Check Digit #
if second_digit == check:
    print('Valid')
else:
    print('Invalid')