let stopwatch = setInterval(currentTime, 1000)

function currentTime() {
    let newDate = new Date()
    document.getElementById('stopwatch').innerHTML = newDate.toLocaleString()
}

