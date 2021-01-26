'''
Lab 09
Unit Converter
Version 3
'''

# Measurement for converting distance
measurement = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
}

print('Welcome to the Unit Converter')

distance = float(input(f'What is the distance? ')) #User inputs distance to convert to meters

measure_from = input('What distance type do you want to input from?\n(ft, mi, m, km, yd, or in)\n') # use the user's input to get the measurement type

measure_to = input('What distance type do you want to output to?\n(ft, mi, m, km, yd, or in)\n')

calc = float(measurement[measure_from] / measurement[measure_to])

print(f'{int(distance)} {measure_from} is {distance * calc:8f} {measure_to}')