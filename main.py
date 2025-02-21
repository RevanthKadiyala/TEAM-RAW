from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")  # Route for index.html
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        print("Received Data:", data)  # Debugging: Print received input

        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        soil_ph = float(data["soilPh"])
        rainfall = float(data["rainfall"])

        input_features = np.array([[temperature, humidity, soil_ph, rainfall]])
        predicted_crop = model.predict(input_features)[0]
        
        print("Predicted Crop:", predicted_crop)  # Debugging: Print output
        
        return jsonify({"recommended_crop": predicted_crop})
    except Exception as e:
        print("Error:", str(e))  # Debugging: Print errors
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
