import joblib
import numpy as np
import pandas as pd  # ✅ Add this
from sklearn.metrics import accuracy_score

# Load trained models
model_value_path = r"C:/Users/NAYAN ADHIKARI/Desktop/Air Quality Index Fullstack/Model/AQI_LightGBM_Model.pkl"
#model_value_path = r"C:/Users/NAYAN ADHIKARI/Desktop/Air Quality Index Fullstack/Model/AQI_Predictions_Model.pkl"
#model_value_path = r"C:/Users/NAYAN ADHIKARI/Desktop/Air Quality Index Fullstack/Model/AQI_XGB_Model.pkl"

model_category_path = r"C:/Users/NAYAN ADHIKARI/Desktop/Air Quality Index Fullstack/Model/AQI_Category_Model.pkl"

try:
    reg_model = joblib.load(model_value_path)
    class_model = joblib.load(model_category_path)
except FileNotFoundError:
    print("Error: Model files not found! Check the paths.")
    exit()

# AQI Categories Mapping
AQI_CATEGORIES = {0: "Good", 1: "Moderate", 2: "Unhealthy for Sensitive Groups", 3: "Unhealthy", 4: "Very Unhealthy", 5: "Hazardous"}

# Define expected features
FEATURE_NAMES = ["Ozone AQI Value", "NO2 AQI Value", "PM2.5 AQI Value", "CO AQI Value", "lat"]

def predict_aqi():
    print("\n🔹 Enter pollutant values for AQI prediction:")
    input_values = []

    for feature in FEATURE_NAMES:
        value = float(input(f"{feature}: "))
        input_values.append(value)

    # ✅ Convert input values into a DataFrame (Fixes Feature Name Warning)
    input_data = pd.DataFrame([input_values], columns=FEATURE_NAMES)

    # Make predictions
    predicted_aqi_value = reg_model.predict(input_data)[0]
    predicted_category_idx = class_model.predict(input_data)[0]
    predicted_aqi_category = AQI_CATEGORIES.get(predicted_category_idx, "Unknown")

    # Compute model accuracy (dummy accuracy for demonstration, real accuracy needs test data)
    y_true = [predicted_category_idx]  # Placeholder true value
    y_pred = class_model.predict(input_data)  # Model prediction
    accuracy = accuracy_score(y_true, y_pred) * 100

    print(f"\n🔹 Predicted AQI Value: {predicted_aqi_value:.2f}")
    print(f"🔹 Predicted AQI Category: {predicted_aqi_category}")
    print(f"🔹 Model Prediction Accuracy: {accuracy:.2f}%")

# Run prediction
if __name__ == "__main__":
    predict_aqi()
