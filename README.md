# 🌍 AQI Prediction Model & Dashboard

## 📌 Project Overview
This project focuses on **predicting Air Quality Index (AQI) using Machine Learning (XGBoost)**. The model is designed to:
- Predict AQI based on input features
- Provide pollutant-specific AQI insights
- Be used in a **Power BI dashboard** for visualization

The model is developed by **Nayan Adhikari**, while the dashboard is being built by a collaborator. We welcome contributions from developers interested in creating a **full-stack web application** for this project. 🚀

## 🏗️ Tech Stack
### **Machine Learning Model**
- XGBoost (AQI Prediction) , LightGBM (AQI Prediction), Random Forest (AQI Prediction), Support Vector Regression (AQI Prediction)
- Pandas, NumPy (Data Processing)
- Scikit-learn (Feature Engineering & Evaluation)

### **Dashboard (Power BI)**
- Power BI Desktop (Visualization)
- DAX for KPI Calculations
- CSV Dataset Integration

### **Future Web Application (Seeking Contributors)**
- **Frontend:** React.js / HTML, CSS, JavaScript
- **Backend:** Flask / FastAPI
- **Database:** PostgreSQL / MongoDB

  ---

## 🚀 Features
✅ **Predict AQI Value & Category** from pollutant data  
✅ **Uses Machine Learning Models:** LightGBM, Random Forest, XGBoost  
✅ **Real-time User Input Support**  
✅ **Performance Metrics:** R² Score, MAE, RMSE  
✅ **Trained on Large AQI Datasets**  
✅ **Deployable as a Web App or API**  

## 📊 Model Performance Comparison
| Model          | R² Score (Higher = Better) | MAE (Lower = Better) | RMSE (Lower = Better) |
|---------------|------------------------|---------------------|---------------------|
| **LightGBM**  | ✅ 0.9982 (Best)       | ✅ 0.3058 (Best)   | ✅ 1.7156 (Best)   |
| **Random Forest** | ❌ 0.9960  | ❌ 1.2711  | ❌ 2.5527  |
| **XGBoost**   | ❌ 0.9819  | ❌ 0.5357  | ❌ 5.4680  |

📌 **Final Model Choice:** **LightGBM** is the best due to highest accuracy.

## 📂 Project Structure
```
Air Quality Index Fullstack/
│
│── Model/
│   ├── AQI_XGB_Model.pkl
│   ├── AQI_Category_Model.pkl
│   ├── AQI_LightGBM_Model.pkl
│   ├── AQI_Predictions_Model.pkl (Random Forest)
│   ├── AQI_svr_Model.pkl
│
│── Src/
│   ├── input.py  # User input for AQI prediction
│   ├── Train_model_LightGBM.ipynb
│   ├── Train_model_Random_Forest.ipynb
│   ├── Train_model_SVR.ipynb
│   ├── Train_model_Xgb.ipynb
│── Data/
│   ├── AQI and Lat Long of Countries_cleaned.csv  # Raw AQI data
│   ├── AQI and Lat Long of Countries.csv 
│   ├── AQI_Predictions.csv 
│── Data/
│   ├── Data_cleaning.ipynb
│   ├── Exploratory_data_cleaning.ipynb
│── Dashboard/
│   ├── AQI.pbix
│── Visualization/
│   ├── AQI_World_Map.html
│   ├── Visualize.ipynb
```
## 🚀 Getting Started

### **1️⃣ Train & Save Model**
```bash
# Install Dependencies
pip install -r requirements.txt

# Train Model & Save
python model/train.py
```
✅ **Model saved as:** `model/aqi_model.pkl`

### **2️⃣ Make Predictions**
```bash
python model/predict.py --input sample_data.csv
```
✅ **Predictions saved in:** `predictions.csv`

---
## 🛠 How to Run
1️⃣ **Install dependencies**:
```bash
pip install lightgbm xgboost numpy pandas scikit-learn joblib
```
2️⃣ **Train the models** (if not already trained):
```bash
python train_dual_models.py
```
3️⃣ **Run manual input for prediction:**
```bash
python input.py
```

## 🔥 Example Prediction
```
🔹 Enter pollutant values for AQI prediction:
Ozone AQI Value: 85
NO2 AQI Value: 60
PM2.5 AQI Value: 110
CO AQI Value: 1.2
lat: 28.61

🔹 Predicted AQI Value: 110.09
🔹 Predicted AQI Category: Very Unhealthy
🔹 Model Prediction Accuracy: 100.00%
```

## 📊 Power BI Dashboard
If you want to analyze AQI data visually:
1️⃣ Open **Power BI Desktop**
2️⃣ Load `AQI_Historical.csv`
3️⃣ Create charts:
   - **AQI World Map** 🗺️
   - **Pollutant Trends** 📉
   - **AQI Category Breakdown** 🏭
4️⃣ Publish & Share 🌍

---

## 🛠️ Future Development: Seeking Contributors
We are looking for **developers interested in transforming this project into a web application**. If you have expertise in **web development (React, Flask, FastAPI, MongoDB, PostgreSQL)** and want to contribute, please join us!

🚀 **Interested? Submit a pull request or contact us!**

---

## 🤝 Contributors
- **Nayan Adhikari** - Machine Learning Model Development 📈
- **Pallabi Ghosh** - Power BI Dashboard 📊

📌 **Want to contribute?** Fork the repo & submit a pull request! 🎉

---

## 📜 License
This project is **open-source** under the **MIT License**. Feel free to use and modify it.

---

## 📞 Contact
📧 **Email:** nayanadhikari1507@gmail.com
🌐 **GitHub:** https://github.com/Nayan-Adhikari


---
🚀 **Built with ❤️ to Improve Air Quality Awareness!** 🌍🔥

