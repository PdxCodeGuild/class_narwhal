def card_check():
    card_num = input("Credit Card Number:  ")
    # Convert the input string into a list of ints
    numbers = [int(n) for n in card_num]
    # Slice off the last digit. That is the check digit.
    check = numbers.pop(-1)
    # Reverse the digits.
    numbers = list(reversed(numbers))
    # Double every other element in the reversed list.
    numbers = [i*2 if i%2 == 0 else i for i in numbers]
    # Subtract nine from numbers over nine.
    numbers = [(num - 9) if num > 9 else num for num in numbers]
    # Sum all values.
    total = sum(numbers)
    # Take the second digit of that sum.
    digit = (total % 10)
    # If that matches the check digit, the whole card number is valid.
    return digit == check

print(card_check())