def is_even(a):
    a = a%2
    if a == 0:
        return True
    else:
        return False

num = int(input('Enter a number: '))

print(f'{num} is an even number!')

print(is_even(num))