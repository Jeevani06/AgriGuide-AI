const score = {LOW: 1, MEDIUM: 2, HIGH: 3};
if (document.getElementById("riskChart") && RISKS.length)
  new Chart(document.getElementById("riskChart"), {type: "line",
    data: {labels: RISKS.map(r => r.crop), datasets: [{label: "Risk (1=Low, 3=High)", data: RISKS.map(r => score[r.level]), borderColor: "#2f8f4e", backgroundColor: "#2f8f4e22", fill: true, tension: .3}]},
    options: {responsive: true, maintainAspectRatio: false, plugins: {legend: {display: false}}, elements: {point: {radius: 3, hoverRadius: 5}}, scales: {y: {min: 0, max: 3, ticks: {stepSize: 1}}}}});
