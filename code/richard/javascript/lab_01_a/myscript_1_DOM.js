// # Richard
// Python Lab 10 - average numbers ... but in javascript
// March 18th, 2021

// alert('hello Richard');


// Version 1 - Take the average by adding the numbers up and dividing by the total


// step 1. write a function that pulls out the contents of the box, 
// turns into numbers, does the math, and display to the screen
function calculateAverage(event) {


// Get the numbers from the input box
let number_input = document.getElementById("number_input")

// console.log the contents of the input box
console.log('The input box contains the following text: ' + number_input.value)

// convert the contents of the input box to numbers
var contents_numeric = number_input.value.split(', ')

// turn the list into a list of numbers
let number_list = []
var i;
for (i = 0; i < contents_numeric.length; i++) {
    //console.log(number_list);
  number_list.push(parseFloat(contents_numeric[i]))
  //console.log(number_list)
}
console.log('The input box contains the following numbers: ' + number_list)


// count how many numbers there are in the list
let length = number_list.length;
console.log('There are: ' + length + ' numbers in the list')

// total the numbers
let total = 0
for (let i=0; i<number_list.length; i++) {
    total = total + number_list[i];
}
console.log('The total of the numbers is: ' + total)


// calcualate the average
let average = total / length
console.log('The average of the numbers is: ' + average)


// update the number in the html to the correct answer
document.getElementById("count").innerHTML = length;
document.getElementById("answer").innerHTML = average;


}

// step 2. Listen for events and execute the function if that event occours
number_input.addEventListener('input', function(event) { // input or keyup
    //if (event.key === 'Enter') {

        calculateAverage()
    //}
})