'''
Lab 09
Unit Converter
Version 1
'''

meters = 0.3048

print('Welcome to the Unit Converter')
distance = float(input('What is the distance in feet? ')) #User inputs distance in feet to convert to meters

calc = distance * meters

print(f'{distance} ft is {distance * meters:.4f} m')