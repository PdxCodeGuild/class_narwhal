def within_10(a):
    diff = a - 100
    if diff >= -10 and diff <= 10:
        return True
    return False 


num = int(input('Enter a number: '))
print('The number you entered is within 10 of 100')
print(within_10(num))