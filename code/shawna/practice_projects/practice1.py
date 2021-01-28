import math
# Instructions: For each practice problem, write a function that returns a value (not just prints it). 
# You can then call the function a couple times to test it, comment those calls out, 
# and move on to the next problem.

#-------1.1-------
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(num):
   return True if num % 2 == 0 else False
print('-' * 40)
print(is_even(9))
#-------1.2-------
# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
    if ((a < 0) and (b > 0)) or ((a > 0) and (b < 0)):
        return True
    else:
        return False
print('-' * 40)
print(f"Positive and negative: {opposite(4, -2)}")
print(f"Negative and positive: {opposite(-4, 2)}")
print(f"Positive and positive: {opposite(4, 2)}")
print(f"Negative and negative: {opposite(-4, -2)}")

#-------1.3-------
# Write a function that returns True if a number within 10 of 100.

def near100(num):
    return True if num in range(90, 111) else False

print('-' * 40)
print(near100(110))

#-------1.4-------
#Write a function that returns the maximum of 3 parameters.

def max(a, b, c):
    group = [a, b, c]
    group.sort()
    max = group[-1]
    return max

print('-' * 40)
print(max(10, 22, 13))

#-------1.4-------
#Print out the powers of 2 from 2^0 to 2^20

def expo(num):
    values =[]
    for i in range (0, 21):
        total = num ** i
        values.append((total))
    return values
    
print('-' * 40)
print(expo(2))