'''
Josh Novac
Python
Lab09
PDX Code Guild
'''

########## verison 4 ##########

# user input
amount = int(input('\nEnter amount: '))
unit_1 = input('\nEnter input unit: ')
unit_2 = input('\nEnter output unit: ')

# unit_1 - multiply
if unit_1 == 'ft':
    meters = amount * 0.3048
elif unit_1 == 'mi':
    meters = amount * 1609.34
elif unit_1 == 'm':
    meters = amount * 1
elif unit_1 == 'km':
    meters = amount * 1000
elif unit_1 == 'yd':
    meters = amount * 0.9144
elif unit_1 == 'in':
    meters = amount * 0.0254

# unit_2 - divide
if unit_2 == 'ft':
    solution = meters / 0.3048
elif unit_2 == 'mi':
    solution = meters / 1609.34
elif unit_2 == 'm':
    solution = meters / 1
elif unit_2 == 'km':
    solution = meters / 1000
elif unit_2 == 'yd':
    solution = meters / 0.9144
elif unit_2 == 'in':
    solution = meters / 0.0254
# prints solution in f string
print(f'\nAnswer: {amount} {unit_1} is {solution} {unit_2}!')