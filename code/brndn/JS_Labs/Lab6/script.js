console.log(new Date())

const second = document.getElementById('second');
const minute = document.getElementById('minute');
const hour = document.getElementById('hour');
const day = document.getElementById('day');
const weekday = document.getElementById('weekday');
const month = document.getElementById('month');
const year = document.getElementById('year');

function clock() {
    var date = new Date();
    var months = new Array();
    months[0] = "January";
    months[1] = "February";
    months[2] = "March";
    months[3] = "April";
    months[4] = "May";
    months[5] = "June";
    months[6] = "July";
    months[7] = "August";
    months[8] = "September";
    months[9] = "October";
    months[10] = "November";
    months[11] = "December";
    var weeks = new Array();
    weeks[1] = "Monday";
    weeks[2] = "Tuesday";
    weeks[3] = "Wednesday";
    weeks[4] = "Thursday";
    weeks[5] = "Friday";
    weeks[6] = "Saturday";
    weeks[7] = "Sunday";
    second.innerText = date.getSeconds();
    minute.innerText = date.getMinutes();
    hour.innerText = date.getHours();
    day.innerText = date.getDate();
    weekday.innerText = weeks[date.getDay()];
    month.innerText = months[date.getMonth()];
    year.innerText = date.getFullYear();
}

window.setInterval(clock, 1000);