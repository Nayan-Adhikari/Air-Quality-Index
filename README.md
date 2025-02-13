# 🌍 AQI Prediction Model & Dashboard

## 📌 Project Overview
This project focuses on **predicting Air Quality Index (AQI) using Machine Learning (XGBoost)**. The model is designed to:
- Predict AQI based on input features
- Provide pollutant-specific AQI insights
- Be used in a **Power BI dashboard** for visualization

The model is developed by **Nayan Adhikari**, while the dashboard is being built by a collaborator **Pallabi Ghosh**. We welcome contributions from developers interested in creating a **full-stack web application** for this project. 🚀

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
│── Model/                                         # Trained ML Model
│   ├── AQI_Predictions.pkl                        # Saved XGBoost Model
│── Data/                                          # AQI Data
│   ├── AQI and Lat Long of Countries.csv          # Raw Dataset
│   ├── AQI and Lat Long of Countries_cleaned.csv  # Cleaned Dataset
│   ├── AQI_Predictions.csv                        # Predicted Dataset
│── Dashboard/                                     # Dashboard Resources
│   ├── AQI_PowerBI.pbix                           # Power BI Report
│── Src/                                           # Source file
│   ├── Train_model.ipynb                          # Training model
│── Visualizations/                                # Visualization
│   ├── AQI_World_Map.html                         # World map
│   ├── Visualize.ipynb                            # Visualize
│── README.md                                      # Project Documentation
## 🚀 Getting Started

### **1️⃣ Train & Save Model**
# Train Model & Save
python Src/Train_model.ipynb
```
✅ **Model saved as:** `Model/AQI_Predictions.pkl`

### **2️⃣ Make Predictions**

✅ **Predictions saved in:** `AQI_Predictions.csv`

---

## 📊 Power BI Dashboard
If you want to analyze AQI data visually:
1️⃣ Open **Power BI Desktop**
2️⃣ Load `AQI and Lat Long of Countries_cleaned.csv`
        `AQI_Predictions.csv`
3️⃣ Create charts:
   - **AQI World Map** 🗺️
   - **Pollutant Trends** 📉
   - **AQI Category Breakdown** 🏭

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
