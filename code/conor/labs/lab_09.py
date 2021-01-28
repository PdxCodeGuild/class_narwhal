# ---- Lab 09 ---- #

# -- Unit Converter -- #

# - Version 1 - #

feet_meters = {1 : 0.3048}

#measurement = feet_meters[1]
#print(measurement)

feet = input("""
What is the distance in 'Feet'? """)
feet = int(feet)

value = feet_meters[1]
output = value * feet
print(f'{feet} is equal to {output:.4f} .')


# - Version 2 - #


conv = {
   'ft' : 0.3048,
    'mi' : 1609.34,
   'm' : 1,
   'km' : 1000
    }

unit = input("""
Is the measurement in ft, mi, m or km? """)

dist = input("""
What is the distance? """)
dist = int(dist)

value = conv[unit]
output = value * dist
print(f'{dist}{unit} is {output:.4f} meters.')

# - Version 3 - #

conv = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
    }

unit = input("""
Is the measurement in ft, mi, m, km, yd or in? """)

dist = input("""
What is the distance? """)
dist = int(dist)

value = conv[unit]
output = value * dist
print(f'{dist}{unit} is {output:.2f} meters.')

# - Version 4 - #

conv = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yd' : 0.9144,
    'in' : 0.0254
    }

dist = input("""
What is the distance? """)
dist = int(dist)

begin_unit = input("""
What unit is the input distant in ft, mi, m, km, yd or in? """)

end_unit = input("""
What is the output unit in ft, mi, m, km, yd or in? """)

value = conv[begin_unit]
output = value * dist

inv_value = conv[end_unit]
inv_output = output / inv_value

print(f'{dist}{begin_unit} is {inv_output:.2f}{end_unit}.')