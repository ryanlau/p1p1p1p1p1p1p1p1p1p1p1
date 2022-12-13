function createCharts(data){
    Object.keys(data).forEach(ticker => {
        createChart(ticker, data[ticker]["bars"])
    });
}
function createChart(ticker, bars) {
    const ctx = document.getElementById(ticker + '-chart')
    console.log(ctx);
    
    new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            fill: 'start',
            data: bars,
            tension: 0.3
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
