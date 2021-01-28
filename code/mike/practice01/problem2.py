def is_positive(a, b):
    if a > b and a != b:
        if a > 0 and b < 0:
            return True
        else:
            return False
    elif b > a:
        if b > 0 and a < 0:
            return True
        else:
            return False
    return False

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

print(is_positive(num1, num2))