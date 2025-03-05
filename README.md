# 🌍 AQI Prediction Model & Dashboard

## 📌 Project Overview
This project focuses on **predicting Air Quality Index (AQI) using Machine Learning (XGBoost)**. The model is designed to:
- Predict AQI based on input features
- Provide pollutant-specific AQI insights
- Be used in a **Power BI dashboard** for visualization

The model is developed by **Nayan Adhikari**, while the dashboard is being built by a collaborator. We welcome contributions from developers interested in creating a **full-stack web application** for this project. 🚀

## 🏗️ Tech Stack
### **Machine Learning Model**
- XGBoost (AQI Prediction)
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

## 📂 Folder Structure
```txt
AQI-Prediction-Model/
│── model/               # Trained ML Model
│   ├── aqi_model.pkl    # Saved XGBoost Model
│   ├── train.py         # Model Training Script
│   ├── predict.py       # AQI Prediction Script
│── dataset/             # AQI Data
│   ├── AQI_Historical.csv # Raw Dataset
│── powerbi/             # Dashboard Resources
│   ├── AQI_PowerBI.pbix # Power BI Report
│── README.md            # Project Documentation
```

---

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

