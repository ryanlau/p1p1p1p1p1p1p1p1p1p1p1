function createCharts(data){
    Object.keys(data).forEach(ticker => {
        createChart(ticker, data[ticker]["bars"], data[ticker]["change"])
    });
}
function createChart(ticker, bars, change) {
    const ctx = document.getElementById(ticker + '-chart')
    console.log(ctx);
    
    new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            fill: 'start',
            data: bars,
            tension: 0.3,
            borderColor: change > 0 ? "#00ff00" : change == 0 ? "#777777" : "#ff0000" ,
            backgroundColor: change > 0 ? "#9eff9e" : change == 0 ? "#c9c9c9" : "#ff9e9e" ,
        }],
    },
    options: {
        elements: {
            point: {
                radius: 0
            }
        },
        scales: {
            x: {
                display: false,
            },
            y: {
                display: false,
                }
        },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                    }
            },

    }
    })
}
