# ---- Practice Problems Fundamentals ---- #

# - Problem 1 - #

def is_even(a):
    if (a % 2) == 0:
        return True
    return False

a = input("Type a number: ")
a = int(a)

print(is_even(a))

# - Problem 2 - #

def opposite(a, b):
    if a >= 0 and b < 0:
        return True
    return False

a = int(input('Please enter your first number: '))
b = int(input('Please enter your second number: '))

print(opposite(a, b))

# - Problem 3 - #

def near_100(num):
    if num in range(10, 100):
        return True
    return False

num = input("Type a number: ")
num = int(num)

print(near_100(num))

# - Problem 4 - #

def maximum(a, b, c):
    max = 0
    for item in (a, b, c):
        if item > max:
            max = item
    return max

a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = int(input('Enter your third number: '))

print(maximum(a, b, c))

# - Problem 5 - #

# - uuuuuhhhmmmm - #