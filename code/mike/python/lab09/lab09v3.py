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

measure_from = input('What distance type do you want to convert from?\n(ft, mi, m, km, yd, or in)\n') # use the user's input to get the measurement type

calc = float(measurement[measure_from] / measurement['m'])

print(f'{int(distance)} {measure_from} is {distance * calc} m')