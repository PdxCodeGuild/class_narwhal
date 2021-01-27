def main():

    choice = 'yes'
    conversion_units = {

            'ft': 0.3048,
            'mi': 1609.34,
            'km': 1000,
            'yd': 0.9144,
            'in': 0.0254,
            'm' : 1.0
    }



    while choice == 'yes':
        
        input_unit = input('Welcome to the unit conversion calculator, please choose from ft, in, yd, km, m, or mi: ')
        distance = input('What distance would you like to convert? ')
        convert_to = input("What unit would you like to convert to (ft, in, yd, km, m, or mi)? ")
        distance = int(distance)
        meters = 0 
        convert_factor = 0

       # Convert input unit to meters 
        if input_unit == 'ft':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        elif input_unit == 'mi':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        elif input_unit == 'km':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        elif input_unit == 'yd':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        elif input_unit == 'in':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        elif input_unit == 'm':
            convert_factor = conversion_units[input_unit]
            meters = distance * convert_factor
        
        # Convert meters to user's desired output unit
        if convert_to == 'ft':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        elif convert_to == 'mi':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        elif convert_to == 'km':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        elif convert_to == 'yd':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        elif convert_to == 'in':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        elif convert_to == 'm':
            convert_factor = conversion_units[convert_to]
            output = meters / convert_factor
        
        output = round(output, 3)
        print(f'{distance} {input_unit} is equal to {output} {convert_to} ')
        choice = input('Would you like to convert another unit (yes/no)? ')
    
    print('Goodbye!')
main()