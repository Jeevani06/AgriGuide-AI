const score = {LOW: 1, MEDIUM: 2, HIGH: 3};
if (document.getElementById("riskChart") && RISKS.length)
  new Chart(document.getElementById("riskChart"), {type: "line",
    data: {labels: RISKS.map((_, i) => "Check " + (i + 1)), datasets: [{label: "Risk (1=Low, 3=High)", data: RISKS.map(r => score[r]), borderColor: "#198754"}]},
    options: {scales: {y: {min: 0, max: 3, ticks: {stepSize: 1}}}}});
