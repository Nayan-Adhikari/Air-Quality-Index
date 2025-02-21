# 🧠 Model Training for AQI Prediction

## 📌 Project Overview
This document explains the **model training process** for the **AQI Prediction Project**. The goal is to develop a **machine learning model** that accurately predicts **Air Quality Index (AQI)** based on pollutant levels and other environmental factors.

## 📂 Dataset Information
- **Source:** Air Quality Index (AQI) datasets from government agencies, OpenAQ API, or Kaggle.
- **Format:** CSV file containing air pollution readings for different locations.
- **Key Features:**
  - `PM2.5 AQI Value`, `NO2 AQI Value`, `CO AQI Value`, `Ozone AQI Value` → Pollutant-specific AQI levels
  - `Temperature`, `Humidity` → Additional environmental factors (if available)
  - `AQI Value` → Target variable

---

## 🚀 Steps for Model Training

### **1️⃣ Load Dataset & Preprocess Data**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("AQI_Historical.csv")

# Select Features & Target
X = df[['PM2.5 AQI Value', 'NO2 AQI Value', 'CO AQI Value', 'Ozone AQI Value']]
y = df['AQI Value']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
✅ **Splits data into training and testing sets to evaluate model performance.**

---

### **2️⃣ Train an XGBoost Model**
```python
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Train Model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")
```
✅ **Trains an optimized XGBoost model and evaluates its accuracy.**

---

### **3️⃣ Save the Trained Model**
```python
import pickle

# Save model to file
with open("aqi_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
```
✅ **Ensures the trained model can be used for predictions in deployment.**

---

### **4️⃣ Load & Use the Model for Predictions**
```python
# Load the saved model
with open("aqi_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

# Example Prediction
new_data = [[45, 20, 0.5, 30]]  # Example: PM2.5, NO2, CO, Ozone
predicted_aqi = loaded_model.predict(new_data)
print("Predicted AQI:", predicted_aqi[0])
```
✅ **Allows the trained model to be used for real-time AQI predictions.**

---

## 🔥 Next Steps: Deployment & Real-Time Predictions
- **Deploy Model:** Serve predictions using Flask/FastAPI.
- **Integrate Live Data:** Fetch real-time AQI readings from APIs.
- **Build a Web App:** Display results in an interactive dashboard.

🔗 **Looking to contribute?** Fork the repo & help improve the model pipeline! 🚀

#MachineLearning #DataScience #AQIPrediction #ModelTraining #XGBoost

