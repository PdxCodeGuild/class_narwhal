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

//alert("hello R")



function addCallback(event) {

// Part 1: Get the inputs from the webpage


// 1. Input number to convert
let number = document.getElementById("number_input").value
console.log('input number: ' + number)


// 2. Units to convert from
let convert_from = document.getElementsByName("units_from")
//console.log(convert_from)
var selected_units_from
for(var i = 0; i < convert_from.length; i++) {
    if(convert_from[i].checked)
        selected_units_from = convert_from[i].value;
 }
console.log('convert from: ' + selected_units_from)


// 3. Units to convert to
let convert_to = document.getElementsByName("units_to")
var selected_units_to
for(var i = 0; i < convert_to.length; i++) {
    if(convert_to[i].checked)
        selected_units_to = convert_to[i].value;
 }
console.log('convert to: ' + selected_units_to)


// 4. Submit button
let calcBtn = document.getElementById("calc")








// Part 2: Convert the number to the correct output


// Determine the conversion unit from original unit to meters
// (feet, miles, meters, kilometers, yards, inches)
let conversion = 0
switch (selected_units_from) {
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
    console.log("Your inputs don't make sense, please refresh and try again.")
} else {
    distance_in_meters = number * conversion
    console.log("The distance in meters is: " + distance_in_meters)
}




// Step 3: Convert output in meters to output in the users chosen output unit

// Determine the conversion unit from meters to input_units_to
// (feet, miles, meters, kilometers, yards, inches)
let conversion_out = 0
switch (selected_units_to) {
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
let distance_output
if (conversion_out === "unknown") {
    console.log("Your inputs don't make sense, please refresh and try again.")
} else {
    distance_output = Math.round( distance_in_meters * conversion_out)
    console.log("The distance in " + selected_units_to + " is: " + distance_output)
}


// Part 3 - Display the correct output to the screen
// input_num, input_unit, output_num, output_unit
document.getElementById("input_num").innerHTML = number;
document.getElementById("input_unit").innerHTML = selected_units_from;
document.getElementById("output_num").innerHTML = distance_output;
document.getElementById("output_unit").innerHTML = selected_units_to;



}



// Recalculate when someone clicks the button
calcBtn.addEventListener('click', addCallback)
calcBtn.addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        addCallback()
    }
})