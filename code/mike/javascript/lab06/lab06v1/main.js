let clock = setInterval(currentTime, 1000)

function currentTime() {
    let newDate = new Date()
    document.getElementById('clock').innerHTML = newDate.toLocaleString()
}