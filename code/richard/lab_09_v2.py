

# Richard
# Lab 9 - Unit conversions
# January 26th, 2021

# https://github.com/PdxCodeGuild/class_narwhal/blob/main/1%20Python/labs/lab09-unit_converter.md



# Without using a dictionary


#########################################
# Version 1
# > what is the distance in feet? 12
# > 12 ft is 3.6576 m
'''
user_input = float(input("What is the distance in feet? "))
# print(user_input)
output = round(user_input * 0.3048, 4)
print(f"{user_input} ft is {output} m")
'''

#########################################
# Version 2, 3, & 4 (the ugly way)
'''
Allow the user to also enter the units. Then depending on the units, 
convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
'''

# Step 1: Get the inputs
dist_input = float(input("What is the number to convert? "))
# print(dist_input)

units_input = input("What are the units of input? (feet, miles, meters, kilometers, yards, inches) ")
# print(units_input)

units_output = input("What are the units of output? (feet, miles, meters, kilometers, yards, inches) ")
# print(units_output)




# Step 2: Calculate the output number in meters
if units_input in ["feet", "miles", "meters", "kilometers", "yards", "inches"]:
    print("Good, thats a unit input I can understand")
else:
    print("Sorry, I need the input to be feet, miles, meters, kilometers, yards, or inches")

if units_input == "feet":
    output = round(dist_input * 0.3048, 4)
elif units_input == "miles":
    output = dist_input * 1609.34
elif units_input == "meters":
    output = dist_input
elif units_input == "yards":
    output = dist_input * 0.9144
elif units_input == "inches":
    output = dist_input * 0.0254
elif units_input == "kilometers":
    output = dist_input * 1000
else: 
    output = "unknown"


# Step 3: convert output in meters to output in the correct unit

if units_output == "feet":
    output = output / 0.3048
elif units_output == "miles":
    output = output / 1609.34
elif units_output == "meters":
    output = output
elif units_output == "kilometers":
    output = output / 1000
elif units_output == "yards":
    output = output * 0.9144
elif units_output == "inches":
    output = output * 0.0254


# round the output
output = round(output, 4)


# Step 4: Print the output
print(f"{dist_input} {units_input} is {output} {units_output}")


