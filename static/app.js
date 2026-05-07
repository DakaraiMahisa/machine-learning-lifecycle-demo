const form = document.getElementById("prediction-form");

const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    temperature: parseFloat(document.getElementById("temperature").value),

    humidity: parseFloat(document.getElementById("humidity").value),

    voltage: parseFloat(document.getElementById("voltage").value),

    vibration: parseFloat(document.getElementById("vibration").value),
  };

  try {
    const response = await fetch("/predict/", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(payload),
    });

    const data = await response.json();

    resultDiv.innerHTML = `Prediction: ${data.prediction}`;
  } catch (error) {
    resultDiv.innerHTML = "Prediction failed.";

    console.error(error);
  }
});
