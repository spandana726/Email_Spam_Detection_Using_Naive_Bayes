document.getElementById("checkButton").addEventListener("click", () => {
  const message = document.getElementById("messageInput").value.trim();
  const resultDiv = document.getElementById("result");

  if (!message) {
    resultDiv.textContent = "Please enter some text or URL.";
    resultDiv.className = "result danger";
    resultDiv.classList.remove("hidden");
    return;
  }

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
  .then(response => response.json())
  .then(data => {
    resultDiv.classList.remove("hidden");
    if (data.result.toLowerCase() === "ham" || data.result === "safe") {
      resultDiv.textContent = "✅ This is SAFE (Ham)";
      resultDiv.className = "result safe";
    } else {
      resultDiv.textContent = "⚠️ This is SPAM / PHISHING!";
      resultDiv.className = "result danger";
    }
  })
  .catch(error => {
    resultDiv.textContent = "❌ Error contacting detection service.";
    resultDiv.className = "result danger";
    resultDiv.classList.remove("hidden");
    console.error("API error:", error);
  });
});
