
function Time() {
    let timeNow = new Date();
    let hours = timeNow.getHours();
    let minutes = timeNow.getMinutes();
    let seconds = timeNow.getSeconds();

    let currentTime = `${hours}:${minutes}:${seconds}`
    let myClock = document.getElementById("clock")

    myClock.innerHTML = currentTime
}