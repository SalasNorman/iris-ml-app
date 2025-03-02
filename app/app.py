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
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        prediction = model.predict(features)[0]
        prediction_text = species_map.get(prediction, "Unknown species")

        # Map prediction to corresponding image
        image_path = f"/static/images/{prediction_text.lower()}.png"
        
        # Render template with prediction and image
        return render_template("index.html", prediction_text=f"Predicted Species: {prediction_text}", image_path=image_path)
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
