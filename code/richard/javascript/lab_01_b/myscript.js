 /* 
Distance conversion lab - originally coded in python... now converting to javascript
Richard
March 19th, 2021

Allow the user to also enter the units. Depending on the units, 
convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
 */

// Step 1: Get the inputs from the user

// What is the number to convert?
let input_number = parseInt(prompt("Enter a number: "))
// alert(input_number)

// What are the units of input? (feet, miles, meters, kilometers, yards, inches)
let input_units_from = prompt("Enter the unit type that you would like to convert FROM: (feet, miles, meters, kilometers, yards, inches)")
//alert(input_units_from)

// What are the units of output? (feet, miles, meters, kilometers, yards, inches)
let input_units_to = prompt("Enter the unit type that you would like to convert TO: (feet, miles, meters, kilometers, yards, inches)")
//alert(input_units_to)

// Tell the user whats about to happen
alert("OK, the plan is to convert " + input_number + " " + input_units_from + " to " + input_units_to )



// Step 2: Calculate the output number in meters


// Determine the conversion unit from original unit to meters
// (feet, miles, meters, kilometers, yards, inches)
let conversion = 0
switch (input_units_from) {
    case "feet": 
        conversion = 0.3048;
        break;
        //alert(conversion)
    case "miles":
        conversion = 1609.34;
        break;
    case "meters":
        conversion = 1;
        break;
    case "kilometers":
        conversion = 1000;
        break;
    case "yards":
        conversion = 1.09361;
        break;
    case "inches":
        conversion = 1/ 39.37;
        break;
    default:
        conversion = "unknown";
  }

// Convert the input number to meters if possible (otherwise tell user to try inputting again)
let distance_in_meters
if (conversion === "unknown") {
    alert("Your inputs don't make sense, please refresh and try again.")
} else {
    distance_in_meters = input_number * conversion
    alert("The distance in meters is: " + distance_in_meters)
}




// Step 3: Convert output in meters to output in the users chosen output unit

// Determine the conversion unit from meters to input_units_to
// (feet, miles, meters, kilometers, yards, inches)
let conversion_out = 0
switch (input_units_to) {
    case "feet": 
        conversion_out = 3.28;
        break;
        //alert(conversion)
    case "miles":
        conversion_out = 0.000621371;
        break;
    case "meters":
        conversion_out = 1;
        break;
    case "kilometers":
        conversion_out = 0.001;
        break;
    case "yards":
        conversion_out = 1.09361;
        break;
    case "inches":
        conversion_out = 39.37;
        break;
    default:
        conversion_out = "unknown";
  }

// Convert the input number to meters if possible (otherwise tell user to try inputting again) and display the output to the user
if (conversion_out === "unknown") {
    alert("Your inputs don't make sense, please refresh and try again.")
} else {
    let distance_output = distance_in_meters * conversion_out
    alert("The distance in " + input_units_to + " is: " + distance_output)
}
