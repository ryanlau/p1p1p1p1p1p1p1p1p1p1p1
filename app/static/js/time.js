const timeEle = document.getElementById("time")

setInterval(() => {
    console.log("fds")
    const d = new Date()
    time = d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
    timeEle.innerHTML = time
}, 15 * 1000);
