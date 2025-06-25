document.getElementById("health-form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const tension = parseFloat(document.getElementById("tension").value);
  const pouls = parseFloat(document.getElementById("pouls").value);
  const temperature = parseFloat(document.getElementById("temperature").value);

  const response = await fetch("/check", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ tension, pouls, temperature })
  });

  const data = await response.json();

  const resultBox = document.getElementById("result");
  const alertsBox = document.getElementById("alerts");
  alertsBox.innerHTML = "";

  resultBox.classList.remove("d-none", "alert-success", "alert-danger");
  resultBox.classList.add(data.alerts.length > 0 ? "alert-danger" : "alert-success");
  resultBox.textContent = data.result;

  data.alerts.forEach(alert => {
    const li = document.createElement("li");
    li.className = "list-group-item";
    li.textContent = alert;
    alertsBox.appendChild(li);
  });
});