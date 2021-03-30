// Richard Farr
// March 25th, 2021


// 0. Experimentation Area
let date_time_now = new Date();
console.log("date_time_now: " + date_time_now)

let time_now = date_time_now.toLocaleTimeString();
console.log("time_now: " + time_now);



// 1. Selectors
const time_area = document.querySelector('.time_area');
console.log(time_area);
console.log("time_area.innerHTML: " + time_area.innerHTML);
time_area.innerHTML=time_now;



// 2. Functions

function myTimer() {
    var d = new Date();
    document.querySelector('.time_area').innerHTML = d.toLocaleTimeString();
  }


// 3. Event Listeners
var myVar = setInterval(myTimer, 1000);
