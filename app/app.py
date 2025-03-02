from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

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

# Prediction route with enhanced validation and user-friendly error
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from form and validate
        data = []
        expected_fields = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        
        # Check if all required fields are present
        for field in expected_fields:
            if field not in request.form:
                return render_template("index.html", error_message="All fields are required")

        # Convert and validate each input
        for field, value in request.form.items():
            if not value.strip():  # Check for empty strings
                return render_template("index.html", error_message=f"{field.replace('_', ' ').title()} cannot be empty")
            if not value.replace(".", "").replace("-", "").isdigit():  # Allow decimals and negatives
                return render_template("index.html", error_message="Numbers can only be entered")
            data.append(float(value))
        
        # Ensure exactly 4 features
        if len(data) != 4:
            return render_template("index.html", error_message="Exactly 4 inputs are required")
        
        # Convert to numpy array for prediction
        features = np.array(data).reshape(1, -1)
        logging.debug(f"Features: {features}")
        
        # Make prediction
        species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
        prediction = model.predict(features)[0]
        prediction_text = species_map.get(prediction, "Unknown species")
        logging.debug(f"Prediction: {prediction_text}")
        
        # Map prediction to corresponding image
        image_path = f"/static/images/{prediction_text.lower()}.png"
        
        # Verify image exists (optional debug step)
        if not os.path.exists(os.path.join(app.static_folder, "images", f"{prediction_text.lower()}.png")):
            logging.warning(f"Image not found: {image_path}")
        
        # Render template with prediction and image (clear error message)
        return render_template("index.html", prediction_text=f"Predicted Species: {prediction_text}", image_path=image_path, error_message=None)
    
    except ValueError as ve:
        logging.error(f"ValueError: {str(ve)}")
        return render_template("index.html", error_message="Numbers can only be entered")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return render_template("index.html", error_message="An error occurred. Please try again")

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)