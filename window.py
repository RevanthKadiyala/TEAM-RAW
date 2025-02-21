import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the trained model
model_path = "model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

print(type(model))

crop_map={
    0:'Rice',1: 'Maize',2: 'Wheat',3: 'Barley',4: 'Cotton',5: 'Soybean',6: 'Oats',7: 'Sugarcane', 
                              8:'Tea',9: 'Coffee',10: 'Jute',11: 'Tobacco',12: 'Groundnut',13: 'Mustard',14: 'Chili', 
                              15:'Potato', 16:'Onion', 17:'Tomato',18: 'Garlic', 19:'Pulses'
}

def predict_crop():
    try:
        # Get user input
        temperature = float(temp_entry.get())
        humidity = float(humidity_entry.get())
        soil_ph = float(soil_ph_entry.get())
        rainfall = float(rainfall_entry.get())
        
        # Prepare input for the model
        input_features = np.array([[temperature, humidity, soil_ph, rainfall]])
        predicted_label=model.predict(input_features)[0]
        predicted_crop = crop_map.get(predicted_label,"unknown crop")
        
        # Display prediction
        result_label.config(text=f"Recommended Crop: {predicted_crop}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# Create GUI window
root = tk.Tk()
root.title("Crop Recommendation System")
root.geometry("400x300")

# Labels and Entry Fields
tk.Label(root, text="Temperature (°C)").pack()
temp_entry = tk.Entry(root)
temp_entry.pack()

tk.Label(root, text="Humidity (%)").pack()
humidity_entry = tk.Entry(root)
humidity_entry.pack()

tk.Label(root, text="Soil pH").pack()
soil_ph_entry = tk.Entry(root)
soil_ph_entry.pack()

tk.Label(root, text="Rainfall (mm)").pack()
rainfall_entry = tk.Entry(root)
rainfall_entry.pack()

# Predict Button
predict_button = tk.Button(root, text="Get Recommended Crop", command=predict_crop)
predict_button.pack(pady=10)

# Label to Display Result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

# Run the application
root.mainloop()
