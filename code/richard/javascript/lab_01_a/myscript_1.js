// # Richard
// Python Lab 10 - average numbers ... but in javascript
// March 18th, 2021

// alert('hello Richard');


// Version 1 - Take the average by adding the numbers up and dividing by the total

// list of numbers to average
let nums = [5, 0, 8, 3, 4, 1, 6]
alert('The numbers are: ' + nums)
// alert('first number: ' + nums[0])

// count how many there are
let length = nums.length
// alert('length is: ' + length)


// total the numbers
let total = 0
for (let i=0; i<nums.length; i++) {
    total = total + nums[i];
}
// alert('total is: ' + total)

// calcualate the average
let average = total / length
alert('average of the numbers is: ' + average)





// Version 2 - Ask the user to enter the numbers one at a time

// Step 1: Get user input and use to create and display the list of numbers

// Step 2: do the math on the number list and display the average