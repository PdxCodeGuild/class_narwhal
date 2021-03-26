let clock = setInterval(timeKeeper, 1000)

function timeKeeper() {
    console.log("clock")
    let timeNow = new Date()
    document.getElementById('clock').innerHTML = timeNow.toLocaleString()
}
