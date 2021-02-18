# Richard
# Lab 9 - Unit conversions
# January 26th, 2021

# https://github.com/PdxCodeGuild/class_narwhal/blob/main/1%20Python/labs/lab09-unit_converter.md

# version 4
# Use a dictionary


# 1. Create a dictionary that I can reference to do the conversions

conversion = {

    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
    }



# 2. Ask the user for inputs

valid_input_output_units = conversion.keys()
# ["ft", "mi", "m", "km", "yard", "inch"]


# Distance to convert
while True:
    try:
        user_input_distance = int(input("what is the distance to convert from? <enter a number> "))
        break
    except ValueError:
        print('try again')
#print(user_input_distance)


while True:
    try:
        user_input_units = input("what are the units to convert from? <enter ft, mi, m, km, yard, inch> ")
        if user_input_units in valid_input_output_units:
            break
        else:
            print("Please retry entering that")
            continue
    except ValueError:
        print('try again')
#print(user_input_units)





while True:
    try:
        user_output_units = input("what are the units to convert to? <enter ft, mi, m, km, yard, inch> ")
        if user_output_units in valid_input_output_units:
            break
        else:
            print("Please retry entering that")
            continue
    except ValueError:
        print('try again')
#print(user_output_units)







# 3. Check to make sure input units and output units are valid.

# variable to check for valid inputs
inputs_valid = user_input_units in conversion.keys() and user_output_units in conversion.keys()

if inputs_valid:
    print("Good, your input units and output units are valid")
else:
    print("sorry, those inputs types do not make sense")


# 4. Create a conversion factor to convert input units to output units

if inputs_valid:
    conversion_factor = conversion[user_input_units] * (1 / conversion[user_output_units])
else:
    conversion_factor = 1
# print(conversion_factor)


# 5. Do the calculations

if inputs_valid: 
    output = round(user_input_distance * conversion_factor, 4)
else:
    output = "a measure of distance that can not be converted to"


# 6. Display the output

print(f"{user_input_distance} {user_input_units} is {output} {user_output_units}.")
