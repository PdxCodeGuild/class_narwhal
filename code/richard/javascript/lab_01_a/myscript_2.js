// # Richard
// Python Lab 10 - average numbers ... but in javascript
// March 18th, 2021

// alert('hello Richard');



// Version 2 - Ask the user to enter the numbers one at a time

// Step 1: Get user input and use to create and display the list of numbers

// start off with an empty list of numbers
let nums = []
alert("the numbers are: " + nums)

// ask the user to add some numbers
let user_input = (prompt("enter a number, or 'done': "))
while (user_input != 'done') {    
    nums.push(parseFloat(user_input))
    //alert("the numbers are now: " + nums)
    user_input = (prompt("enter a number, or 'done': "))
}


// display the numbers entered to the user
alert('The numbers are: ' + nums)
// alert('first number: ' + nums[0])






// Step 2: do the math on the number list and display the average

// count how many there are
let length = nums.length
// alert('length is: ' + length)


// total the numbers
let total = 0
for (let i=0; i<nums.length; i++) {
    total = total + nums[i];
}
// alert('total is: ' + total)

// calcualate & display the average of the numbers
let average = total / length
alert('average of the numbers is: ' + average)