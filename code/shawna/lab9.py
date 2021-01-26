while True:
    user_quantity = (input('Please enter the amount of distance you would like to convert: '))
    user_units = input('What is the unit of measurment you are converting from? \nPlease enter in feet, inches, yards, miles, meters, or kilometers. ')
    user_output = input('What is the unit of measurment you are converting to? \nPlease enter in feet, inches, yards, miles, meters, or kilometers. ')
        
    conversion = {
        'feet':  0.3048, 
        'miles': 1609.34,
        'meters': 1,
        'kilometers': 1000,
        'yards': 0.9144,
        'inches': 0.0254
    }

    def to_meters(quantity, from_unit):
        """Converts user quantity into meters"""

        meters = (conversion.get(from_unit) * (quantity))
        return meters

    def from_meters(meters, to_unit):
        """Converts quantity from meters into user selected output"""

        output = (meters / conversion.get(to_unit))
        return output

    first_conversion = (to_meters(user_quantity, user_units))
    result = (round (from_meters(first_conversion, user_output), 4))

    print(result)

    #Asks user if they would like to convert another number
    repeat = (input('Would you like to convert another? Y/N: ')).upper
    if repeat == 'N':
        break