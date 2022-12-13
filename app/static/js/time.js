const timeEle = document.getElementById("time")

setTimeout(() => {
    const d = new Date()
    time = d.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
    timeEle.innerHTML = time
}, 1 * 1000)
