async function checkNews() {
    const newsText = document.getElementById('newsText').value;
    const resultDiv = document.getElementById('result');

    if (!newsText) {
        alert("Please enter some news text!");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: newsText })
        });

        const data = await response.json();
        if (data.prediction) {
            resultDiv.innerText = "Prediction: " + data.prediction;
            resultDiv.style.color = data.prediction === "Fake" ? "red" : "green";
        } else if (data.error) {
            resultDiv.innerText = "Error: " + data.error;
            resultDiv.style.color = "orange";
        }
    } catch (error) {
        console.error(error);
        resultDiv.innerText = "Error connecting to API";
        resultDiv.style.color = "orange";
    }
}

