# Flask API: app.py

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

# Define the path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../data/model.pkl")

# Load the trained model
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
else:
    raise FileNotFoundError("model.pkl not found. Ensure the model is trained and saved correctly.")

# Initialize Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from form
        data = [float(x) for x in request.form.values()]
        features = np.array(data).reshape(1, -1)
        # Map numerical predictions to species names
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        prediction = model.predict(features)[0]

        # Convert numeric prediction to species name
        prediction_text = species_map.get(prediction, "Unknown species")

        return render_template("index.html", prediction_text=f"Predicted Species: {prediction_text}")

        
        return render_template("index.html", prediction_text=f"Predicted Species: {prediction}")
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
