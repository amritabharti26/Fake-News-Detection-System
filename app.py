# app.py
import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# ------------------------------
# Setup Flask app
# ------------------------------
app = Flask(__name__)
CORS(app)  # Enable CORS
logging.basicConfig(level=logging.INFO)

# ------------------------------
# Load Model and Vectorizer
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder where app.py is
model_path = os.path.join(BASE_DIR, "fake_news_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    logging.info("Model and vectorizer loaded successfully.")
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
    raise e
except Exception as e:
    logging.error(f"Error loading model/vectorizer: {e}")
    raise e

# ------------------------------
# Prediction Endpoint
# ------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        news_text = data['text']
        logging.info(f"Received text for prediction: {news_text}")

        # Vectorize input text
        vectorized_text = vectorizer.transform([news_text])

        # Predict
        prediction = model.predict(vectorized_text)[0]

        # Convert numeric prediction to readable label
        prediction_label = "Fake" if prediction == 0 else "Real"

        return jsonify({"prediction": prediction_label})

    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

# ------------------------------
# Run the App
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)


