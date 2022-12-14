const timeEle = document.getElementById("time")

setInterval(setTime, 1 * 1000);

function setTime() {
    const d = new Date()
    time = d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
    timeEle.innerHTML = time
}

setTime()
